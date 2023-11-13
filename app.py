# First part of the prompt is the CREATE TABLE statement
# Then is the instructions with CoT
# Finally is some 

import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



cherry_picked_ids = [3, 6, 104, 149, 105, 109, 152, 144, 175, 219, 232]
create_data_sql_path = "FIBEN_Queries.json"

sample_id = 0


