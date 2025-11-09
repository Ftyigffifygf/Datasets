"""Web interface for Medical Vector Database"""
from flask import Flask, render_template, request, jsonify
import yaml
import json
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent.parent))

app = Flask(__name__)

# Load data
def load_data():
    with open("config/disease_taxonomy.yaml") as f:
        taxonomy = yaml.safe_load(f)
    
    with open("config/disease_clinical_details.yaml") as f:
        clinical = yaml.safe_load(f)
    
    with open("config/disease_datasets.yaml") as f:
        datasets = yaml.safe_load(f)
    
    db_path = Path("data/disease_database.json")
    disease_db = {}
    if db_path.exists():
        with open(db_path) as f:
            disease_db = json.load(f)
    
    return taxonomy, clinical, datasets, disease_db

taxonomy, clinical, datasets, disease_db = load_data()


@app.route('/')
def index():
    """Home page"""
    stats = {
        'total_diseases': len(disease_db),
        'total_datasets': sum(len(ds) for ds in datasets.values()),
        'categories': len(taxonomy),
        'clinical_details': sum(len(d) for d in clinical.values())
    }
    return render_template('index.html', stats=stats)


@app.route('/diseases')
def list_diseases():
    """List all diseases"""
    category = request.args.get('category', None)
    
    if category:
        diseases = {k: v for k, v in disease_db.items() 
                   if v.get('category') == category}
    else:
        diseases = disease_db
    
    return render_template('diseases.html', diseases=diseases, category=category)


@app.route('/disease/<disease_id>')
def disease_detail(disease_id):
    """Disease detail page"""
    disease = disease_db.get(disease_id, {})
    
    # Get clinical details
    disease_key = disease.get('name', '').lower().replace(' ', '_').replace('(', '').replace(')', '')
    clinical_info = None
    
    for category, disease_list in clinical.items():
        if disease_key in disease_list:
            clinical_info = disease_list[disease_key]
            break
    
    return render_template('disease_detail.html', 
                         disease=disease, 
                         clinical=clinical_info,
                         disease_id=disease_id)


@app.route('/datasets')
def list_datasets():
    """List all datasets"""
    return render_template('datasets.html', datasets=datasets)


@app.route('/search')
def search():
    """Search diseases"""
    query = request.args.get('q', '').lower()
    
    if not query:
        return jsonify([])
    
    results = []
    for disease_id, disease_info in disease_db.items():
        if query in disease_info.get('name', '').lower():
            results.append({
                'id': disease_id,
                'name': disease_info.get('name'),
                'category': disease_info.get('category')
            })
    
    return jsonify(results[:20])


@app.route('/api/disease/<disease_id>')
def api_disease(disease_id):
    """API endpoint for disease data"""
    disease = disease_db.get(disease_id, {})
    
    if not disease:
        return jsonify({'error': 'Disease not found'}), 404
    
    return jsonify(disease)


@app.route('/api/search')
def api_search():
    """API endpoint for search"""
    query = request.args.get('q', '').lower()
    category = request.args.get('category', None)
    
    results = []
    for disease_id, disease_info in disease_db.items():
        if category and disease_info.get('category') != category:
            continue
        
        if query in disease_info.get('name', '').lower():
            results.append({
                'id': disease_id,
                'name': disease_info.get('name'),
                'category': disease_info.get('category'),
                'has_datasets': disease_info.get('has_datasets', False)
            })
    
    return jsonify(results)


@app.route('/categories')
def categories():
    """List all categories"""
    cats = {}
    for disease_id, disease_info in disease_db.items():
        cat = disease_info.get('category', 'unknown')
        if cat not in cats:
            cats[cat] = 0
        cats[cat] += 1
    
    return render_template('categories.html', categories=cats)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
