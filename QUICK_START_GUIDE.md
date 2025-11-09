# 🚀 Quick Start Guide - Medical Disease Vector Database

## 📊 Database Overview

**Current State:** 1,865+ diseases across 61+ medical specialties

---

## ⚡ Quick Commands

### Search for a Disease
```bash
python scripts/search_individual_disease.py "disease_name"
```

**Examples:**
```bash
python scripts/search_individual_disease.py "diabetes type 2"
python scripts/search_individual_disease.py "rheumatoid arthritis"
python scripts/search_individual_disease.py "chronic kidney disease"
```

### List Datasets by Category
```bash
python scripts/list_datasets_by_condition.py "category_name"
```

**Examples:**
```bash
python scripts/list_datasets_by_condition.py "hematology"
python scripts/list_datasets_by_condition.py "cardiology"
python scripts/list_datasets_by_condition.py "oncology"
```

### Show Database Statistics
```bash
python scripts/show_dataset_stats.py
python scripts/show_expansion_summary.py
```

### Advanced Search
```bash
python scripts/advanced_disease_search.py --category "specialty" --severity "level"
```

---

## 🆕 New Specialties (Super Expansion)

| # | Specialty | Diseases | Key Focus |
|---|-----------|----------|-----------|
| 1 | Hematology Expanded | 46 | Blood disorders, anemias, clotting |
| 2 | Nephrology Expanded | 36 | Kidney diseases |
| 3 | Hepatology Expanded | 34 | Liver diseases |
| 4 | Rheumatology Expanded | 40 | Arthritis, autoimmune |
| 5 | Endocrinology Expanded | 38 | Hormonal disorders |
| 6 | Infectious Diseases Expanded | 47 | Infections |
| 7 | Gastroenterology Expanded | 42 | GI disorders |
| 8 | Pediatrics Expanded | 39 | Childhood diseases |
| 9 | Geriatrics | 29 | Age-related diseases |
| 10 | Emergency Medicine | 34 | Trauma, acute care |
| 11 | Sleep Medicine | 25 | Sleep disorders |
| 12 | Allergy & Immunology | 29 | Allergies, immunodeficiency |
| 13 | Pain Medicine | 27 | Chronic pain |
| 14 | Sports Medicine | 24 | Sports injuries |
| 15 | Occupational Medicine | 22 | Work-related diseases |

---

## 🔍 Common Search Examples

### Hematology
```bash
python scripts/search_individual_disease.py "sickle cell anemia"
python scripts/search_individual_disease.py "hemophilia a"
python scripts/search_individual_disease.py "multiple myeloma"
```

### Nephrology
```bash
python scripts/search_individual_disease.py "chronic kidney disease stage 3"
python scripts/search_individual_disease.py "iga nephropathy"
python scripts/search_individual_disease.py "diabetic nephropathy"
```

### Hepatology
```bash
python scripts/search_individual_disease.py "hepatitis c chronic"
python scripts/search_individual_disease.py "non alcoholic fatty liver"
python scripts/search_individual_disease.py "cirrhosis alcoholic"
```

### Rheumatology
```bash
python scripts/search_individual_disease.py "rheumatoid arthritis severe"
python scripts/search_individual_disease.py "systemic lupus erythematosus"
python scripts/search_individual_disease.py "gout chronic"
```

### Endocrinology
```bash
python scripts/search_individual_disease.py "diabetes type 1"
python scripts/search_individual_disease.py "graves disease"
python scripts/search_individual_disease.py "cushing syndrome"
```

### Sleep Medicine
```bash
python scripts/search_individual_disease.py "obstructive sleep apnea severe"
python scripts/search_individual_disease.py "narcolepsy type 1"
python scripts/search_individual_disease.py "insomnia chronic"
```

### Pain Medicine
```bash
python scripts/search_individual_disease.py "complex regional pain syndrome"
python scripts/search_individual_disease.py "fibromyalgia syndrome"
python scripts/search_individual_disease.py "chronic migraine"
```

---

## 🌐 Web Interface

### Start the Web Application
```bash
python src/web/app.py
```

Then open your browser to: **http://localhost:5000**

---

## 🔧 Setup & Installation

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Setup Environment
```bash
cp .env.example .env
# Edit .env with your configuration
```

### 3. Start Vector Database
```bash
docker-compose up -d
```

### 4. Setup Collections
```bash
python scripts/setup_disease_collections.py
```

### 5. Ingest Sample Data
```bash
python scripts/ingest_sample.py
```

---

## 📚 Documentation Files

### Getting Started
- **README.md** - Main documentation
- **QUICK_START_GUIDE.md** - This file
- **USAGE.md** - Detailed usage instructions

### Database Information
- **COMPLETE_DATABASE_SUMMARY.md** - Complete overview
- **SUPER_EXPANSION_SUMMARY.md** - Super expansion details
- **NEW_SPECIALTIES_GUIDE.md** - New specialties reference

### Disease Information
- **INDIVIDUAL_DISEASES_GUIDE.md** - Disease-specific info
- **DISEASE_CLASSIFICATION.md** - Disease taxonomy
- **DISEASE_DATASETS.md** - Dataset mappings

### Technical Documentation
- **DEPLOYMENT.md** - Deployment guide
- **ULTIMATE_SYSTEM_GUIDE.md** - Complete system docs
- **ARCHITECTURE.md** - System architecture

---

## 🎯 Common Use Cases

### 1. Find Datasets for a Disease
```bash
# Search for the disease
python scripts/search_individual_disease.py "diabetes type 2"

# List all datasets for that category
python scripts/list_datasets_by_condition.py "endocrinology"
```

### 2. Explore a Medical Specialty
```bash
# List all diseases in the specialty
python scripts/list_datasets_by_condition.py "hematology"

# Search for specific diseases
python scripts/search_individual_disease.py "leukemia"
```

### 3. Research Multiple Diseases
```bash
# Search for related diseases
python scripts/search_disease_subtypes.py "diabetes"
python scripts/search_disease_subtypes.py "arthritis"
```

### 4. Get Database Statistics
```bash
# Show overall stats
python scripts/show_dataset_stats.py

# Show expansion summary
python scripts/show_expansion_summary.py
```

---

## 💡 Tips & Tricks

### Search Tips
- Use specific disease names for better results
- Try both full names and abbreviations
- Search by category for broader results
- Use advanced search for filtered results

### Performance Tips
- Use batch queries for multiple searches
- Cache frequently accessed results
- Use the web interface for interactive exploration
- Leverage the API for programmatic access

### Data Tips
- Check dataset availability before analysis
- Review data quality metrics
- Consider multi-modal data for comprehensive analysis
- Use disease subtypes for granular research

---

## 🆘 Troubleshooting

### Database Connection Issues
```bash
# Check if Qdrant is running
docker ps

# Restart Qdrant
docker-compose restart qdrant
```

### Search Returns No Results
- Check spelling of disease name
- Try searching by category instead
- Use broader search terms
- Check if the disease is in the database

### Performance Issues
- Reduce batch size for queries
- Check system resources
- Optimize vector database settings
- Consider scaling infrastructure

---

## 📞 Support

### Documentation
- Check the documentation files listed above
- Review the examples in this guide
- Explore the scripts directory

### Community
- GitHub Issues: [repository_url]
- Discord: [discord_url]
- Forum: [forum_url]

### Enterprise Support
- Email: support@example.com
- Phone: +1-XXX-XXX-XXXX

---

## 🎉 Quick Stats

```
╔═══════════════════════════════════════════════╗
║  Medical Disease Vector Database v4.0         ║
╠═══════════════════════════════════════════════╣
║  Diseases:        1,865+                      ║
║  Specialties:     61+                         ║
║  Datasets:        90+                         ║
║  Data Volume:     500+ TB                     ║
║  Samples:         2.5M+                       ║
╚═══════════════════════════════════════════════╝
```

---

## 🚀 Next Steps

1. **Explore the database** - Try the search commands above
2. **Read the documentation** - Check out the detailed guides
3. **Start the web interface** - Interactive exploration
4. **Build your application** - Use the API for integration
5. **Contribute** - Help expand the database further

---

**Ready to explore the world's most comprehensive medical disease database!** 🎊

*Last Updated: November 9, 2025*
*Version: 4.0 (Super Expansion)*
