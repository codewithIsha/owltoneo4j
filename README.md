
> 🚀 *A gateway into biomedical graph mining using Python — from ontology to visualization in Neo4j.*

---

## 📌 Project Overview

This project demonstrates how to convert an OWL (Web Ontology Language) ontology — particularly biomedical — into a structured **property graph** using **Neo4j**.  
It reflects my internship work involving semantic data engineering, biomedical domain modeling, and practical Neo4j automation using Python.

### 🔬 Internship Project Highlights:

- Biomedical ontology parsing
- OWL to Neo4j conversion
- Graph schema modeling
- Automation of entity-relationship generation
- Bonus: Office hierarchy modeling using Cypher

---

## 📚 Supporting Research

Explore my extended research work in biomedical graph modeling:

🔗 [🧠 Research Findings Repository](https://github.com/Jeri-jose/kgraph/tree/main/Sneha)

---
---

## 🧪 Technologies Used

| Tool         | Purpose                           |
|--------------|------------------------------------|
| 🐍 Python     | Scripting and automation           |
| 📦 `owlready2` | Load and parse OWL ontologies     |
| 🔌 `py2neo`   | Neo4j Python driver                |
| 🕸️ Neo4j      | Graph database to store RDF triples |
| 🧩 Protégé    | Design OWL ontology visually       |

---

## ✨ Creating or Editing the Ontology with Protégé

The OWL ontology used in this project (`ontology.owl`) was created and edited using [Protégé](https://protege.stanford.edu/), a popular open-source tool for working with OWL files.

### 🧬 Why Use Protégé?

- Easy visual creation of **Classes**, **Individuals**, and **Object Properties**
- Ability to define **hierarchies**, **relations**, and **annotations**
- Exports directly to `.owl` format compatible with this script

### 🛠 Example Design Steps

1. Open Protégé and create a new OWL ontology
2. Add biomedical concepts under **Classes**
3. Add specific examples under **Individuals**
4. Define relationships under **Object Properties**
5. Save the file as `ontology.owl` and place it in this project directory

---

# 🦉➡️ 🧠 OWL to Neo4j Converter

This Python script converts an OWL ontology into a Neo4j graph database. It creates nodes for classes, individuals, and object properties, and establishes relationships between them in the Neo4j database.


## Installation

1. Clone the repository:
```https://github.com/codewithIsha/owltoneo4j.git```

2. Install the required packages:
```pip install owlready2 py2neo```

3. Run the script:
```python main.py```

4. The script will connect to Neo4j, clear any existing data (MAKE SURE THERE IS NO USEFUL DATA ONBOARD THE DB), create nodes for classes and individuals, and establish relationships for object properties.

5. Once the script finishes, you can use the Neo4j browser or client to explore and query the converted ontology in the Neo4j database.

   
## 🚀 Usage

1. Make sure you have an OWL ontology file (`ontology.owl`) in the project directory.

2. Update the Neo4j connection details in the script (`graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))`) to match your Neo4j server configuration.
   
## 🔗 Prerequisites

- Neo4j running locally (desktop or server)
- Python 3.x
- Required packages:

## 🧪 Bonus: Office Knowledge Graph
Run cipherQueriesOfiice.txt in Neo4j Browser to create a company structure with:

- Departments, branches, employees

- Roles: Manager, Intern, etc.

- Relations like HAS, TYPES, SUB_DEPARTMENT


### ▶️ Run the Script

```bash
python main.py
pip install owlready2 py2neo

```
## 📜 License

This project is licensed under the [MIT License](LICENSE).




