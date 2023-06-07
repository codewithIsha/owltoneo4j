# OWL to Neo4j Converter

This Python script converts an OWL ontology into a Neo4j graph database. It creates nodes for classes, individuals, and object properties, and establishes relationships between them in the Neo4j database.

## Installation

1. Clone the repository:
```https://github.com/codewithIsha/owltoneo4j.git```

2. Install the required packages:
```pip install owlready2 py2neo```

## Usage

1. Make sure you have an OWL ontology file (`ontology.owl`) in the project directory.

2. Update the Neo4j connection details in the script (`graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))`) to match your Neo4j server configuration.

3. Run the script:
```python main.py```

4. The script will connect to Neo4j, clear any existing data (MAKE SURE THERE IS NO USEFUL DATA ONBOARD THE DB), create nodes for classes and individuals, and establish relationships for object properties.

5. Once the script finishes, you can use the Neo4j browser or client to explore and query the converted ontology in the Neo4j database.

## License

This project is licensed under the [MIT License](LICENSE).

Please note that you should replace `"your-username"` and `"your-repository"` with your actual GitHub username and repository name, respectively.



