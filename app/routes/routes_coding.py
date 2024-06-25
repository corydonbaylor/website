from flask import render_template, request
from app import app
from neo4j import GraphDatabase
import os

# coding routes
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the environment variables
URI = os.environ.get("GRAPH_URL", "bolt://localhost:7687")  # Default value as fallback
AUTH = (os.environ.get("NEO4J_USERNAME", "neo4j"), os.environ.get("GRAPH_KEY"))

driver = GraphDatabase.driver(URI, auth=AUTH)
# adding comment
# another comment
@app.route('/coding')
def coding():
    return render_template('pages/coding/coding.html', title='Analytics',  pad='p-0')


@app.route('/coding/getwiki')
def getwiki():
    return render_template('pages/coding/getwiki.html', title='getwiki')

@app.route('/coding/graph', methods=['POST', 'GET'])
def graph():
    if request.method == 'POST':
        name = request.form['name']
        results = get_person_by_name(name)
        return render_template('pages/coding/graph.html', results=results, name = name)

    return render_template('pages/coding/graph.html')

URI = "neo4j+s://3ac296a1.databases.neo4j.io"  # Replace with your database URI
AUTH = ("neo4j", "MM3vgv_s21kntE_GtdEUVu5TkGMG_ueOW3Qmy44QvGQ") 

driver = GraphDatabase.driver(URI, auth=AUTH)

def get_person_by_name(name):
    query = """match (u:User {name: $name})-[:PURCHASED]->(p:Product)<-[:PURCHASED]-(peer:User)-[:PURCHASED]->(rec:Product)
    where not (u)-[:PURCHASED]->(rec)
    return rec.name as title, count(*) as count
    order by count desc
    limit 4;"""    
    with driver.session() as session:
        results = session.run(query, name=name)
        records = [record.data() for record in results]
    
    return records