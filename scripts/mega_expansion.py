#!/usr/bin/env python3
"""
MEGA EXPANSION - Add 500+ more diseases across 15+ new specialties
Expands from 1,353 to 1,900+ diseases
"""

import yaml
from pathlib import Path

def load_current_taxonomy():
    """Load current disease taxonomy"""
    taxonomy_path = Path("config/expanded_disease_taxonomy.yaml")
    with open(taxonomy_path, 'r') as f:
        data = yaml.safe_load(f)
        # If data is None or doesn't have the expected structure, create it
        if data is None:
            data = {}
        if 'disease_categories' not in data:
            data = {'disease_categories': data if isinstance(data, dict) else {}}
        return data

def create_mega_expansion():
    """Create massive expansion with 15+ new specialties"""
    
    mega_categories = {
        # 1. HEMATOLOGY EXPANDED (45 diseases)
        "hematology_expanded": {
            "name": "Hematology Expanded",
            "diseases": [
                # Anemias
                "iron_deficiency_anemia", "vitamin_b12_deficiency_anemia", "folate_deficiency_anemia",
                "aplastic_anemia", "hemolytic_anemia_autoimmune", "hemolytic_anemia_hereditary",
                "sickle_cell_anemia", "thalassemia_major", "thalassemia_minor", "thalassemia_intermedia",
                "anemia_of_chronic_disease", "sideroblastic_anemia", "pernicious_anemia",
                # Bleeding Disorders
                "hemophilia_a", "hemophilia_b", "von_willebrand_disease_type1", "von_willebrand_disease_type2",
                "von_willebrand_disease_type3", "factor_v_leiden", "prothrombin_mutation",
                "disseminated_intravascular_coagulation", "thrombocytopenia_immune", "thrombocytopenia_drug_induced",
                # Clotting Disorders
                "deep_vein_thrombosis", "pulmonary_embolism", "antiphospholipid_syndrome",
                "protein_c_deficiency", "protein_s_deficiency", "antithrombin_deficiency",
                # Blood Cancers
                "acute_lymphoblastic_leukemia", "acute_myeloid_leukemia", "chronic_lymphocytic_leukemia",
                "chronic_myeloid_leukemia", "hairy_cell_leukemia", "multiple_myeloma",
                "waldenstrom_macroglobulinemia", "hodgkin_lymphoma", "non_hodgkin_lymphoma_diffuse",
                "non_hodgkin_lymphoma_follicular", "burkitt_lymphoma", "mantle_cell_lymphoma",
                # Other
                "polycythemia_vera", "essential_thrombocythemia", "myelofibrosis"
            ]
        },
        
        # 2. NEPHROLOGY EXPANDED (38 diseases)
        "nephrology_expanded": {
            "name": "Nephrology Expanded",
            "diseases": [
                # Chronic Kidney Disease
                "chronic_kidney_disease_stage1", "chronic_kidney_disease_stage2", "chronic_kidney_disease_stage3a",
                "chronic_kidney_disease_stage3b", "chronic_kidney_disease_stage4", "chronic_kidney_disease_stage5",
                "end_stage_renal_disease",
                # Glomerular Diseases
                "iga_nephropathy", "membranous_nephropathy", "minimal_change_disease",
                "focal_segmental_glomerulosclerosis", "membranoproliferative_glomerulonephritis",
                "rapidly_progressive_glomerulonephritis", "goodpasture_syndrome",
                # Tubular Disorders
                "acute_tubular_necrosis", "fanconi_syndrome", "renal_tubular_acidosis_type1",
                "renal_tubular_acidosis_type2", "renal_tubular_acidosis_type4", "bartter_syndrome",
                "gitelman_syndrome", "liddle_syndrome",
                # Other Kidney Diseases
                "polycystic_kidney_disease_autosomal_dominant", "polycystic_kidney_disease_autosomal_recessive",
                "nephrotic_syndrome", "nephritic_syndrome", "diabetic_nephropathy",
                "hypertensive_nephropathy", "lupus_nephritis", "alport_syndrome",
                "renal_artery_stenosis", "renal_vein_thrombosis", "hydronephrosis",
                "pyelonephritis_acute", "pyelonephritis_chronic", "interstitial_nephritis"
            ]
        },
        
        # 3. HEPATOLOGY EXPANDED (35 diseases)
        "hepatology_expanded": {
            "name": "Hepatology Expanded",
            "diseases": [
                # Viral Hepatitis
                "hepatitis_a", "hepatitis_b_acute", "hepatitis_b_chronic", "hepatitis_c_acute",
                "hepatitis_c_chronic", "hepatitis_d", "hepatitis_e",
                # Chronic Liver Disease
                "cirrhosis_alcoholic", "cirrhosis_cryptogenic", "cirrhosis_biliary_primary",
                "cirrhosis_biliary_secondary", "liver_failure_acute", "liver_failure_chronic",
                # Fatty Liver Disease
                "non_alcoholic_fatty_liver_disease", "non_alcoholic_steatohepatitis",
                "alcoholic_fatty_liver", "alcoholic_hepatitis",
                # Autoimmune Liver Disease
                "autoimmune_hepatitis_type1", "autoimmune_hepatitis_type2",
                "primary_biliary_cholangitis", "primary_sclerosing_cholangitis",
                # Metabolic Liver Disease
                "hemochromatosis", "wilson_disease", "alpha1_antitrypsin_deficiency",
                "gilbert_syndrome", "crigler_najjar_syndrome", "dubin_johnson_syndrome",
                # Other
                "budd_chiari_syndrome", "portal_hypertension", "hepatorenal_syndrome",
                "hepatopulmonary_syndrome", "hepatic_encephalopathy"
            ]
        },
        
        # 4. RHEUMATOLOGY EXPANDED (42 diseases)
        "rheumatology_expanded": {
            "name": "Rheumatology Expanded",
            "diseases": [
                # Inflammatory Arthritis
                "rheumatoid_arthritis_early", "rheumatoid_arthritis_established", "rheumatoid_arthritis_severe",
                "psoriatic_arthritis_oligoarticular", "psoriatic_arthritis_polyarticular",
                "psoriatic_arthritis_spondylitis", "ankylosing_spondylitis", "reactive_arthritis",
                "enteropathic_arthritis", "juvenile_idiopathic_arthritis",
                # Crystal Arthropathies
                "gout_acute", "gout_chronic", "gout_tophaceous", "pseudogout",
                "calcium_pyrophosphate_deposition_disease",
                # Connective Tissue Diseases
                "systemic_lupus_erythematosus_mild", "systemic_lupus_erythematosus_moderate",
                "systemic_lupus_erythematosus_severe", "scleroderma_limited", "scleroderma_diffuse",
                "mixed_connective_tissue_disease", "sjogren_syndrome_primary", "sjogren_syndrome_secondary",
                "polymyositis", "dermatomyositis", "inclusion_body_myositis",
                # Vasculitis
                "giant_cell_arteritis", "takayasu_arteritis", "polyarteritis_nodosa",
                "kawasaki_disease", "granulomatosis_with_polyangiitis", "eosinophilic_granulomatosis",
                "microscopic_polyangiitis", "henoch_schonlein_purpura", "behcet_disease",
                # Other
                "polymyalgia_rheumatica", "fibromyalgia", "osteoarthritis_generalized",
                "septic_arthritis", "lyme_arthritis"
            ]
        },
        
        # 5. ENDOCRINOLOGY EXPANDED (40 diseases)
        "endocrinology_expanded": {
            "name": "Endocrinology Expanded",
            "diseases": [
                # Diabetes
                "diabetes_type1_new_onset", "diabetes_type1_established", "diabetes_type2_early",
                "diabetes_type2_advanced", "diabetes_gestational", "diabetes_mody",
                "diabetes_neonatal", "diabetes_secondary_pancreatic",
                # Thyroid Disorders
                "hypothyroidism_subclinical", "hypothyroidism_overt", "hyperthyroidism_subclinical",
                "hyperthyroidism_overt", "graves_disease", "hashimoto_thyroiditis",
                "thyroid_nodule_benign", "thyroid_nodule_malignant", "thyroiditis_subacute",
                "thyroiditis_postpartum",
                # Adrenal Disorders
                "addison_disease", "cushing_syndrome_pituitary", "cushing_syndrome_adrenal",
                "cushing_syndrome_ectopic", "primary_aldosteronism", "pheochromocytoma",
                "adrenal_insufficiency_secondary", "congenital_adrenal_hyperplasia",
                # Pituitary Disorders
                "acromegaly", "prolactinoma", "growth_hormone_deficiency",
                "diabetes_insipidus_central", "diabetes_insipidus_nephrogenic",
                "syndrome_inappropriate_adh", "hypopituitarism", "pituitary_adenoma_nonfunctioning",
                # Parathyroid & Bone
                "hyperparathyroidism_primary", "hyperparathyroidism_secondary", "hypoparathyroidism",
                "osteoporosis_postmenopausal"
            ]
        },
        
        # 6. INFECTIOUS_DISEASES_EXPANDED (50 diseases)
        "infectious_diseases_expanded": {
            "name": "Infectious Diseases Expanded",
            "diseases": [
                # Bacterial Infections
                "tuberculosis_pulmonary", "tuberculosis_extrapulmonary", "tuberculosis_miliary",
                "tuberculosis_latent", "mycobacterium_avium_complex", "leprosy",
                "lyme_disease_early", "lyme_disease_disseminated", "lyme_disease_late",
                "syphilis_primary", "syphilis_secondary", "syphilis_tertiary", "syphilis_congenital",
                "gonorrhea", "chlamydia_trachomatis", "bacterial_vaginosis",
                # Viral Infections
                "hiv_acute", "hiv_chronic", "aids", "ebv_mononucleosis", "cmv_infection",
                "herpes_simplex_type1", "herpes_simplex_type2", "varicella_zoster_chickenpox",
                "varicella_zoster_shingles", "measles", "mumps", "rubella",
                "dengue_fever", "zika_virus", "west_nile_virus", "rabies",
                # Fungal Infections
                "candidiasis_oral", "candidiasis_esophageal", "candidiasis_invasive",
                "aspergillosis_invasive", "aspergillosis_allergic", "cryptococcosis",
                "histoplasmosis", "coccidioidomycosis", "pneumocystis_pneumonia",
                # Parasitic Infections
                "malaria_falciparum", "malaria_vivax", "toxoplasmosis", "giardiasis",
                "cryptosporidiosis", "amebiasis"
            ]
        },
        
        # 7. GASTROENTEROLOGY_EXPANDED (45 diseases)
        "gastroenterology_expanded": {
            "name": "Gastroenterology Expanded",
            "diseases": [
                # Esophageal Disorders
                "gerd_mild", "gerd_severe", "barrett_esophagus", "esophagitis_eosinophilic",
                "esophageal_stricture", "achalasia", "esophageal_spasm", "esophageal_varices",
                # Stomach Disorders
                "gastritis_acute", "gastritis_chronic", "peptic_ulcer_gastric", "peptic_ulcer_duodenal",
                "helicobacter_pylori_infection", "gastroparesis", "gastric_outlet_obstruction",
                # Inflammatory Bowel Disease
                "crohn_disease_ileal", "crohn_disease_colonic", "crohn_disease_ileocolonic",
                "ulcerative_colitis_proctitis", "ulcerative_colitis_left_sided",
                "ulcerative_colitis_pancolitis", "microscopic_colitis",
                # Functional Disorders
                "irritable_bowel_syndrome_diarrhea", "irritable_bowel_syndrome_constipation",
                "irritable_bowel_syndrome_mixed", "functional_dyspepsia",
                # Small Intestine
                "celiac_disease", "small_intestinal_bacterial_overgrowth", "lactose_intolerance",
                "whipple_disease", "tropical_sprue", "short_bowel_syndrome",
                # Colon Disorders
                "diverticulosis", "diverticulitis_uncomplicated", "diverticulitis_complicated",
                "colonic_polyps_adenomatous", "colonic_polyps_hyperplastic",
                "ischemic_colitis", "pseudomembranous_colitis",
                # Pancreas
                "pancreatitis_acute", "pancreatitis_chronic", "pancreatic_insufficiency"
            ]
        },
        
        # 8. PEDIATRICS_EXPANDED (40 diseases)
        "pediatrics_expanded": {
            "name": "Pediatrics Expanded",
            "diseases": [
                # Congenital Disorders
                "down_syndrome", "turner_syndrome", "klinefelter_syndrome", "fragile_x_syndrome",
                "prader_willi_syndrome", "angelman_syndrome", "williams_syndrome",
                # Developmental Disorders
                "autism_spectrum_disorder", "attention_deficit_hyperactivity_disorder",
                "intellectual_disability_mild", "intellectual_disability_moderate",
                "cerebral_palsy_spastic", "cerebral_palsy_dyskinetic", "cerebral_palsy_ataxic",
                # Metabolic Disorders
                "phenylketonuria", "maple_syrup_urine_disease", "galactosemia",
                "glycogen_storage_disease_type1", "mucopolysaccharidosis_type1",
                "gaucher_disease", "tay_sachs_disease", "niemann_pick_disease",
                # Respiratory
                "bronchiolitis", "croup", "epiglottitis", "pertussis",
                "respiratory_syncytial_virus", "cystic_fibrosis_pediatric",
                # Infectious
                "kawasaki_disease_pediatric", "scarlet_fever", "fifth_disease",
                "hand_foot_mouth_disease", "roseola",
                # Other
                "failure_to_thrive", "pyloric_stenosis", "intussusception",
                "hirschsprung_disease", "necrotizing_enterocolitis", "retinopathy_of_prematurity"
            ]
        },
        
        # 9. GERIATRICS (30 diseases)
        "geriatrics": {
            "name": "Geriatrics",
            "diseases": [
                # Cognitive Disorders
                "alzheimer_disease_early", "alzheimer_disease_moderate", "alzheimer_disease_severe",
                "vascular_dementia", "lewy_body_dementia", "frontotemporal_dementia",
                "mild_cognitive_impairment", "delirium_hyperactive", "delirium_hypoactive",
                # Mobility Disorders
                "sarcopenia", "frailty_syndrome", "osteoporosis_senile",
                "falls_recurrent", "gait_disorder", "balance_disorder",
                # Sensory
                "presbycusis", "presbyopia", "age_related_macular_degeneration_dry",
                "age_related_macular_degeneration_wet",
                # Urinary
                "urinary_incontinence_stress", "urinary_incontinence_urge",
                "urinary_incontinence_overflow", "benign_prostatic_hyperplasia_severe",
                # Other
                "pressure_ulcer_stage1", "pressure_ulcer_stage2", "pressure_ulcer_stage3",
                "pressure_ulcer_stage4", "polypharmacy", "malnutrition_elderly"
            ]
        },
        
        # 10. EMERGENCY_MEDICINE (35 diseases)
        "emergency_medicine": {
            "name": "Emergency Medicine",
            "diseases": [
                # Trauma
                "traumatic_brain_injury_mild", "traumatic_brain_injury_moderate", "traumatic_brain_injury_severe",
                "spinal_cord_injury_complete", "spinal_cord_injury_incomplete",
                "rib_fracture", "pneumothorax_traumatic", "hemothorax", "cardiac_tamponade",
                "splenic_rupture", "liver_laceration", "bowel_perforation",
                # Shock
                "hypovolemic_shock", "cardiogenic_shock", "septic_shock", "anaphylactic_shock",
                "neurogenic_shock",
                # Acute Events
                "acute_coronary_syndrome", "stroke_ischemic_acute", "stroke_hemorrhagic_acute",
                "pulmonary_embolism_massive", "aortic_dissection_type_a", "aortic_dissection_type_b",
                # Toxicology
                "acetaminophen_overdose", "salicylate_overdose", "opioid_overdose",
                "benzodiazepine_overdose", "tricyclic_antidepressant_overdose",
                "carbon_monoxide_poisoning", "cyanide_poisoning",
                # Environmental
                "hypothermia", "hyperthermia", "heat_stroke", "frostbite"
            ]
        },
        
        # 11. SLEEP_MEDICINE (25 diseases)
        "sleep_medicine": {
            "name": "Sleep Medicine",
            "diseases": [
                "obstructive_sleep_apnea_mild", "obstructive_sleep_apnea_moderate",
                "obstructive_sleep_apnea_severe", "central_sleep_apnea",
                "complex_sleep_apnea", "insomnia_acute", "insomnia_chronic",
                "narcolepsy_type1", "narcolepsy_type2", "idiopathic_hypersomnia",
                "restless_legs_syndrome", "periodic_limb_movement_disorder",
                "rem_sleep_behavior_disorder", "non_rem_sleep_arousal_disorder",
                "nightmare_disorder", "sleep_related_eating_disorder",
                "circadian_rhythm_disorder_delayed", "circadian_rhythm_disorder_advanced",
                "circadian_rhythm_disorder_shift_work", "circadian_rhythm_disorder_jet_lag",
                "sleep_related_hypoventilation", "sleep_related_hypoxemia",
                "parasomnia_sleepwalking", "parasomnia_sleep_terrors", "bruxism"
            ]
        },
        
        # 12. ALLERGY_IMMUNOLOGY (30 diseases)
        "allergy_immunology": {
            "name": "Allergy & Immunology",
            "diseases": [
                # Allergic Diseases
                "allergic_rhinitis_seasonal", "allergic_rhinitis_perennial",
                "allergic_conjunctivitis", "atopic_dermatitis_mild", "atopic_dermatitis_moderate",
                "atopic_dermatitis_severe", "contact_dermatitis_allergic", "contact_dermatitis_irritant",
                # Food Allergies
                "peanut_allergy", "tree_nut_allergy", "milk_allergy", "egg_allergy",
                "wheat_allergy", "soy_allergy", "fish_allergy", "shellfish_allergy",
                # Drug Allergies
                "penicillin_allergy", "sulfa_allergy", "nsaid_hypersensitivity",
                # Immunodeficiencies
                "common_variable_immunodeficiency", "selective_iga_deficiency",
                "x_linked_agammaglobulinemia", "severe_combined_immunodeficiency",
                "chronic_granulomatous_disease", "wiskott_aldrich_syndrome",
                # Other
                "mastocytosis", "hereditary_angioedema", "acquired_angioedema",
                "eosinophilic_esophagitis"
            ]
        },
        
        # 13. PAIN_MEDICINE (28 diseases)
        "pain_medicine": {
            "name": "Pain Medicine",
            "diseases": [
                # Neuropathic Pain
                "diabetic_neuropathy_painful", "postherpetic_neuralgia", "trigeminal_neuralgia",
                "complex_regional_pain_syndrome_type1", "complex_regional_pain_syndrome_type2",
                "peripheral_neuropathy_painful", "phantom_limb_pain",
                # Musculoskeletal Pain
                "chronic_low_back_pain", "chronic_neck_pain", "myofascial_pain_syndrome",
                "temporomandibular_joint_disorder", "costochondritis",
                # Headache
                "migraine_chronic", "tension_headache_chronic", "cluster_headache_chronic",
                "medication_overuse_headache", "cervicogenic_headache",
                # Visceral Pain
                "chronic_abdominal_pain", "chronic_pelvic_pain", "interstitial_cystitis",
                "chronic_pancreatitis_pain",
                # Other
                "fibromyalgia_syndrome", "central_sensitization_syndrome",
                "chronic_widespread_pain", "cancer_pain_chronic",
                "sickle_cell_pain_chronic", "chronic_postoperative_pain"
            ]
        },
        
        # 14. SPORTS_MEDICINE (25 diseases)
        "sports_medicine": {
            "name": "Sports Medicine",
            "diseases": [
                # Overuse Injuries
                "rotator_cuff_tendinopathy", "tennis_elbow", "golfer_elbow",
                "patellar_tendinopathy", "achilles_tendinopathy", "plantar_fasciitis",
                "shin_splints", "stress_fracture_tibia", "stress_fracture_metatarsal",
                # Acute Injuries
                "anterior_cruciate_ligament_tear", "posterior_cruciate_ligament_tear",
                "medial_collateral_ligament_tear", "lateral_collateral_ligament_tear",
                "meniscus_tear_medial", "meniscus_tear_lateral",
                "ankle_sprain_grade1", "ankle_sprain_grade2", "ankle_sprain_grade3",
                "shoulder_dislocation", "shoulder_separation",
                # Other
                "concussion_grade1", "concussion_grade2", "concussion_grade3",
                "exercise_induced_asthma"
            ]
        },
        
        # 15. OCCUPATIONAL_MEDICINE (22 diseases)
        "occupational_medicine": {
            "name": "Occupational Medicine",
            "diseases": [
                # Respiratory
                "asbestosis", "silicosis", "coal_worker_pneumoconiosis",
                "berylliosis", "byssinosis", "occupational_asthma",
                "hypersensitivity_pneumonitis_occupational",
                # Musculoskeletal
                "carpal_tunnel_syndrome_occupational", "repetitive_strain_injury",
                "vibration_white_finger", "low_back_pain_occupational",
                # Dermatologic
                "occupational_contact_dermatitis", "occupational_urticaria",
                # Toxic Exposures
                "lead_poisoning", "mercury_poisoning", "arsenic_poisoning",
                "pesticide_poisoning", "solvent_exposure_chronic",
                # Other
                "noise_induced_hearing_loss", "radiation_exposure_chronic",
                "heat_stress_occupational", "shift_work_disorder"
            ]
        }
    }
    
    return mega_categories

def main():
    print("Loading current taxonomy...")
    taxonomy = load_current_taxonomy()
    
    current_count = sum(len(cat.get('diseases', [])) for cat in taxonomy['disease_categories'].values())
    print(f"Starting with {current_count} diseases")
    
    print("\nCreating MEGA expansion...")
    mega_categories = create_mega_expansion()
    
    # Add new categories
    added_count = 0
    for cat_id, cat_data in mega_categories.items():
        if cat_id not in taxonomy['disease_categories']:
            print(f"Adding {cat_id}...")
            taxonomy['disease_categories'][cat_id] = cat_data
            disease_count = len(cat_data['diseases'])
            print(f"  Added {disease_count} diseases")
            added_count += disease_count
    
    # Save updated taxonomy
    output_path = Path("config/expanded_disease_taxonomy.yaml")
    with open(output_path, 'w') as f:
        yaml.dump(taxonomy, f, default_flow_style=False, sort_keys=False)
    
    # Calculate final stats
    final_count = sum(len(cat.get('diseases', [])) for cat in taxonomy['disease_categories'].values())
    total_categories = len(taxonomy['disease_categories'])
    
    print("\n" + "="*80)
    print("MEGA EXPANSION COMPLETE!")
    print("="*80)
    print(f"Added: {added_count} new diseases")
    print(f"Total: {final_count} diseases")
    print("="*80)
    
    # Show top categories
    category_counts = [(name, len(data.get('diseases', []))) 
                      for name, data in taxonomy['disease_categories'].items()]
    category_counts.sort(key=lambda x: x[1], reverse=True)
    
    print(f"\nTop 25 Categories by Disease Count:")
    for i, (name, count) in enumerate(category_counts[:25], 1):
        print(f"  {i:2d}. {name}: {count} diseases")
    
    print(f"\nTotal Categories: {total_categories}")

if __name__ == "__main__":
    main()
