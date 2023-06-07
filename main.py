from owlready2 import *
from py2neo import Graph, Node, Relationship

# Load the OWL ontology
onto = get_ontology("ontology.owl").load()

# Connect to Neo4j
graph = Graph("bolt://localhost:7687", auth=("neo4j", "graphdbms"))

# Clear existing data in Neo4j
graph.delete_all()

# Create nodes for classes and individuals
class_nodes = {}  # Dictionary to store class nodes

for onto_class in onto.classes():
    class_name = onto_class.name

    if class_name not in class_nodes:
        class_node = Node("Class", name=class_name)  # Create a unique "Class" node
        class_nodes[class_name] = class_node
        graph.create(class_node)

    for individual in onto_class.instances():
        individual_node = Node("Individual", name=individual.name)  # Create an "Individual" node
        graph.create(individual_node)

        # Create relationship between the individual and its class
        relationship = Relationship(individual_node, "INSTANCE_OF", class_nodes[class_name])
        graph.create(relationship)

    # Create relationships between classes
    for parent_class in onto_class.is_a:
        parent_name = parent_class.name

        if parent_name not in class_nodes:
            parent_node = Node("Class", name=parent_name)
            class_nodes[parent_name] = parent_node
            graph.create(parent_node)
        else:
            parent_node = class_nodes[parent_name]

        relationship = Relationship(class_nodes[class_name], "SUBCLASS_OF", parent_node)
        graph.create(relationship)

# Create relationships for object properties
for onto_prop in onto.object_properties():
    prop_name = onto_prop.name
    for source_inst, target_inst in onto_prop.get_relations():
        source_node = Node("Individual", name=source_inst.name)  # Create an "Individual" node for the source
        target_node = Node("Individual", name=target_inst.name)  # Create an "Individual" node for the target
        graph.create(source_node)
        graph.create(target_node)

        # Create relationship between the source and target individuals
        relationship = Relationship(source_node, prop_name, target_node)
        graph.create(relationship)


