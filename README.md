### Prolog to Neo4j Family Network Converter

This Python script facilitates the transformation of familial data from Prolog knowledge bases into a Neo4j graph database. It leverages Neo4j's graph database capabilities to model familial relationships, such as parent-child connections, derived from Prolog facts and rules.

#### Prerequisites:
- Python 3.x
- Neo4j Desktop or Neo4j Server installed and running
- pytholog and Neo4j Python driver (`neo4j`) installed via pip

#### How to Use:
1. Ensure Neo4j is running, and note down the Bolt URI and authentication credentials.
2. Prepare your Prolog family relations knowledge base file (`family-relation.pl`) and a text file (`family-relation.txt`) containing extracted facts and rules.
3. Update the script with your Neo4j URI, authentication details, and file paths.
4. Execute the script to initiate the conversion process.

#### Description:
- **connect_neo4j(uri, authentication):** Establishes a connection to the Neo4j database using the provided URI and authentication credentials.
- **read_prologfile(path):** Reads the Prolog knowledge base file and initializes a `KnowledgeBase` object using the `pytholog` library.
- **extract_facts_and_rules(filepath, pattern):** Parses the provided text file to extract facts and rules using a specified pattern.
- **create_nodes(facts, session):** Creates nodes in the Neo4j database representing individuals with their corresponding attributes derived from Prolog facts.
- **create_relationships(session, facts):** Generates relationships between nodes based on parent-child connections inferred from Prolog rules.

#### Example Usage:
```python
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
