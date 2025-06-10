"""
1. What is the total production capacity of the generators in the model 
2. What are the nominal voltages of the windings of the transformer NL_TR2_2 (ID: _2184f365-8cd5-4b5d-8a28-9d68603bb6a4)
3. What is permanently allowed limit for line segment NL-Line_5 (ID: _e8acf6b6-99cb-45ad-b8dc-16c7866a4ddc ) and temporarily allowed. What is difference between those limits.
4. Which generator is set as slack in the model? Why does model need slack node?
5. Find mistakes in the model (both semantic, power system related and logical errors are present)

"""
#This script was used in order to check errors that appeared when trying to read the xml file
from rdflib import Graph

g = Graph()

g.parse(r"C:\Users\Pili\Downloads\colour-checker-detection-develop\colour-checker-detection-develop\RCC_Tasks\20210325T1530Z_1D_NL_EQ_001.xml")

v = g.serialize(format="xml")

