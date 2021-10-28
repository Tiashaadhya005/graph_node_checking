from neo4j import GraphDatabase
import json

class Neo4jConnection:
    def __init__(self, uri,db,password):
        self.__uri = uri
        self.__user="neo4j"
        self.__password=password
        self.__driver = None
        self.session = None
        self.constraint_done = False
        self.__db=db
        try:
            self.__driver = GraphDatabase.driver(self.__uri, auth=(self.__user, self.__password))
        except Exception as e:
            print("Failed to create the driver:", e)
    
    def close(self):
        if self.__driver is not None:
            self.__driver.close()

    def query(self, query, db=None):
        assert self.__driver is not None, "Driver not initialized!"
        response = None
        self.session = self.__driver.session(database=db) if db is not None else self.__driver.session()
        response = list(self.session.run(query))
        return response

    def create_pc_relation(self,data,g):
        unique_constraint_for_prod_comp= "CREATE CONSTRAINT UniqueCompId ON (pc:prod_comp) ASSERT g.prod_compId IS UNIQUE"
        create_pc_node_query = [
            "MERGE (pc {id:\""+str(data['id'])+"\" })",
            "MERGE (pc {logo_path:\""+str(data['logo_path'])+"\"})",
            "MERGE (pc {name:\""+data['name']+"\" })",
            "MERGE (g {origin_country:\""+str(data['origin_country'])+"\"})",
        ]
        rel_with_prod_comp= "MATCH (g:genre), (pc:prod_comp) MERGE (g)-[r:Production_companies]->(pc) RETURN g, pc"
        try:
            if not self.constraint_done:
                self.query(unique_constraint_for_prod_comp, 'neo4j')
        except Exception as e:
        #     if e.code == 'Neo.ClientError.Schema.EquivalentSchemaRuleAlreadyExists':
        #         self.constraint_done=True
        #     else:
             print(e)
        for i in range(len(create_pc_node_query)):
            response = self.query(create_pc_node_query[i], 'neo4j')
        #response = self.query(g, 'neo4j')
        response = self.query(rel_with_prod_comp, 'neo4j')

    def create_genre_relation(self,data,g):
        unique_constraint_for_genre= "CREATE CONSTRAINT UniqueGenreId ON (ge:genre) ASSERT ge.genreId IS UNIQUE"
        create_genre_node_query = [
            "MERGE (ge:genre {id:\""+str(data['id'])+"\" })",
            "MERGE (ge:genre {name:\""+str(data['name'])+"\"})",
        ]
        rel_with_genre= "MATCH (g:genre), (ge:genre) MERGE (g)-[r:genres]->(ge) RETURN g, ge"
        try:
            if not self.constraint_done:
                self.query(unique_constraint_for_genre, 'neo4j')
        except Exception as e:
        #     if e.code == 'Neo.ClientError.Schema.EquivalentSchemaRuleAlreadyExists':
        #         self.constraint_done=True
        #     else:
             print(e)
        for i in range(len(create_genre_node_query)):
            response = self.query(create_genre_node_query[i], 'neo4j')
        response = self.query(rel_with_genre, 'neo4j')

    def create_prod_coun_relation(self,data,g):
        unique_constraint_for_prod_coun= "CREATE CONSTRAINT UniqueProdCounId ON (pco:prod_coun) ASSERT pco:ProdCounId IS UNIQUE"
        create_prod_coun_node_query = [
            "MERGE (pco:prod_coun {iso_3166_1:\""+str(data['iso_3166_1'])+"\" })",
            "MERGE (pco:prod_coun {name:\""+str(data['name'])+"\"})",
        ]
        rel_with_prod_coun= "MATCH (g:genre), (pco:prod_coun) MERGE (g)-[r:production_countries]->(pco) RETURN g, pco"
        try:
            if not self.constraint_done:
                self.query(unique_constraint_for_prod_coun, 'neo4j')
        except Exception as e:
        #     if e.code == 'Neo.ClientError.Schema.EquivalentSchemaRuleAlreadyExists':
        #         self.constraint_done=True
        #     else:
            print(e)
        for i in range(len(create_prod_coun_node_query)):
            response = self.query(create_prod_coun_node_query[i], 'neo4j')
        response = self.query(rel_with_prod_coun, 'neo4j')

    def create_spoken_language_relation(self,data,g):
        unique_constraint_for_language= "CREATE CONSTRAINT UniqueLanguageId ON (sl:soken_language) ASSERT sl:LanguageId IS UNIQUE"
        create_language_node_query = [
            "MERGE (sl:soken_language {iso_639_1:\""+str(data['iso_639_1'])+"\" })",
            "MERGE (sl:soken_language {english_name:\""+str(data['english_name'])+"\"})",
            "MERGE (sl:soken_language {name:\""+str(data['name'])+"\" })",
        ]
        rel_with_language= "MATCH (g:genre), (sl:soken_language) MERGE (g)-[r:spoken_language]->(sl) RETURN g, sl"
        try:
            if not self.constraint_done:
                self.query(unique_constraint_for_language, 'neo4j')
        except Exception as e:
        #     if e.code == 'Neo.ClientError.Schema.EquivalentSchemaRuleAlreadyExists':
        #         self.constraint_done=True
        #     else:
             print(e)
        for i in range(len(create_language_node_query)):
            response = self.query(create_language_node_query[i], 'neo4j')
        response = self.query(rel_with_language, 'neo4j')
        

    def create_movie_node(self, data):
        print("creating..........")
        unique_constraint = "CREATE CONSTRAINT UniqueGenreId ON (g:genre) ASSERT g.genreId IS UNIQUE"
        create_movie_node_query = [
            "MERGE (g {adult:\""+str(data['adult'])+"\" })",
            "MERGE (g {backdrop_path:\""+str(data['backdrop_path'])+"\"})",
            "MERGE (g {belongs_to_collection:\""+str(data['belongs_to_collection'])+"\"});",
            "MERGE (g {budget:\""+str(data['budget'])+"\" }) return g",
            # "MERGE (g:genre)",
            # "MERGE (g:prod_company)",          
            #"MERGE (g {genre:{name:\""+str(data['genres'][1])+"\", genreId:\""+str(data['genres'][0])+"\"} }) return g",
            "MERGE (g {homepage:\""+str(data['homepage'])+"\" }) return g",
            "MERGE (g {id:\""+str(data['id'])+"\" }) return g",
            "MERGE (g {imdb_id:\""+str(data['imdb_id'])+"\" }) return g",
            "MERGE (g {original_language:\"" +str(data['original_language'])+"\" }) return g",
            "MERGE (g {original_title:\""+str(data['original_title'])+"\" }) return g",
            "MERGE (g {overview:\""+str(data['overview'])+"\" }) return g",
            "MERGE (g {popularity:\""+str(data['popularity'])+"\"}) return g",
            "MERGE (g {poster_path:\""+str(data['poster_path'])+"\" }) return g",
            "MERGE (g {release_date:\""+str(data['release_date'])+"\" }) return g",
            "MERGE (g {revenue:\""+str(data['revenue'])+"\" }) return g",
            "MERGE (g {runtime:\""+str(data['runtime'])+"\" }) return g",
            "MERGE (g {status:\""+str(data['status'])+"\" }) return g",
            "MERGE (g {tagline:\""+str(data['tagline'])+"\" }) return g",
            "MERGE (g {title:\""+str(data['title'])+"\" }) return g",
            "MERGE (g {video:\""+str(data['video'])+"\" }) return g",
            "MERGE (g {vote_average:\""+str(data['vote_average'])+"\" }) return g",
            "MERGE (g {vote_count:\""+str(data['vote_count'])+"\" }) return g",
            "MERGE (g {is_processed:\""+str(data['is_processed'])+"\" }) return g",
            #"MERGE (g: production_companies{name:\"" + str(data['production_companies']) + "\", genreId:"+str(data['id'])+ "\", logo_path:+str(data[])"}) return g",
            
        ]
        
        try:
            try:
                if not self.constraint_done:
                    self.query(unique_constraint, 'neo4j')
            except Exception as e:
                if e.code == 'Neo.ClientError.Schema.EquivalentSchemaRuleAlreadyExists':
                    self.constraint_done=True
                else:
                    raise e
            for i in range(len(create_movie_node_query)):
                print(create_movie_node_query[i])
                response = self.query(create_movie_node_query[i], 'neo4j')
            
            for pc_ind in range(len(data['production_companies'])):
                prod_comp=data['production_companies'][pc_ind]
                g_com="MATCH (g:genre)"
                self.create_pc_relation(prod_comp,g_com)

            for g_ind in range(len(data['genres'])):
                genre=data['genres'][g_ind]
                g_com="MATCH (g:genre)"
                self.create_genre_relation(genre,g_com)

            for pcou_ind in range(len(data['production_countries'])):
                pcoun=data['production_countries'][pcou_ind]
                g_com="MATCH (g:genre)"
                self.create_prod_coun_relation(pcoun,g_com)
            
            for sl_ind in range(len(data['spoken_languages'])):
                spoken_language=data['spoken_languages'][sl_ind]
                g_com="MATCH (g:genre)"
                self.create_spoken_language_relation(spoken_language,g_com)
                
        except Exception as e:
            #if not e.code == 'Neo.ClientError.Schema.ConstraintValidationFailed':
            print("Query Error: ", e)
            #response = e.message
        finally:
            if self.session is not None:
                self.session.close()
        return response

if __name__ == "__main__":
    conn = Neo4jConnection(uri="bolt://localhost:7687", db="neo4j",password="tiasha_neo")
    with open('movie_data.json') as f:
        data = json.load(f)
    #print(data)
    genres=data['genres']


    # for i in tqdm(genres):
    result = conn.create_movie_node(data)




    # production_companies" : [
	# 	{
	# 		"id" : 1378,
	# 		"logo_path" : null,
	# 		"name" : "International Apollo Films",
	# 		"origin_country" : ""
	# 	},

    # arr=[]
            # gen_query="MERGE (g {genre:["
            # for genre_ind in range(len(data['genres'])):
            #     genre=data['genres'][genre_ind]
            #     gen_query+="{genreId:\""+str(genre['id'])+"\" , genre_name: \""+str(genre['name'])+"\" },"
            # gen_query=gen_query+" ] )"
            # print(gen_query)
            # response = self.query(gen_query, 'neo4j')

#password-tiasha_neo