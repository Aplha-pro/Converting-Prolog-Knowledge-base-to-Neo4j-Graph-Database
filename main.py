from neo4j import GraphDatabase
from pytholog import KnowledgeBase
import re
 
class FamilyNetwork:
    def __init__(self):
        pass
 
    def connect_neo4j(self, uri, authentication):
        graphdb = GraphDatabase.driver(uri, auth=authentication)
        session = graphdb.session()
        return session
 
    def read_prologfile(self, path):
        knowledge_base = KnowledgeBase('Family Network')
        knowledge_base.from_file(path)
        return knowledge_base

    def extract_facts_and_rules(self, filepath, pattern):
        ext_facts = []
        ext_rules = []
        with open(filepath, 'r') as file:
            for line in file:
                if re.match(pattern, line.strip()):
                    ext_rules.append(line.strip())
                else:
                    ext_facts.append(line.strip())
        return ext_facts, ext_rules
    
    def get_predicate_and_name(self, fact):
        if '(' in fact:
            predicate, arguments = fact.split('(')
            predicate = predicate.strip()
            arguments = arguments[:-2].strip()
        else:
            predicate = fact.strip()
            arguments = ''
        return predicate, arguments


    def create_nodes(self, facts, session):
        for fact in facts:
            fact = str(fact)
            predicate, argument = self.get_predicate_and_name(fact)
            print(f'Predicate {predicate} and Name {argument}')
            query = f"CREATE (n:Person {{name: '{argument}', gender: '{predicate}'}})"
            session.run(query) 
        
    def create_relationships(self, session, facts):
        pattern = "^parent\((.*?),(.*?)\)"
        for fact in facts:
            found = re.findall(pattern, fact)
            if found:
                for group in found:
                    parent = group[0].strip()
                    child = group[1].strip()
                    print(f"Parent: {parent} and Child: {child}")
                    relationship_query=f'''
                                        MATCH (p:Person {{name: '{parent}'}}), (c:Person {{name: '{child}'}})
                                        CREATE (p)-[:is_a_parent_of]->(c)
                                        '''
                    session.run(relationship_query)            
        
 
if __name__ == "__main__":
    obj = FamilyNetwork()
 
    uri = "bolt://localhost:7687"
    auth = ('neo4j', '12345678')
    
    session = obj.connect_neo4j(uri, auth)
    knowledge_base = obj.read_prologfile(path='family-relation.pl')
    
    file_path = "family-relation.txt"
    pattern = '^\w+\(.*?\)\s*:-.*?\.'
    
    facts, rules = obj.extract_facts_and_rules(file_path, pattern)
    obj.create_nodes(facts, session)
    obj.create_relationships(session, facts)

