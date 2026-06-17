import pandas as pd
import google.generativeai as genai

# ==========================================
# GEMINI CONFIGURATION
# ==========================================

GOOGLE_API_KEY="YOUR_API_KEY"

genai.configure(api_key=GOOGLE_API_KEY)

# ==========================================
# LOAD DATASETS
# ==========================================

food_df = pd.read_csv("data/food_business_india.csv")
scholarship_df = pd.read_csv("data/scholarships.csv")
maharashtra_df = pd.read_csv("data/maharashtra_schemes.csv")

# ==========================================
# FOOD SEARCH
# ==========================================

def search_food(query):

    keywords = [
        "bakery",
        "restaurant",
        "cafe",
        "food truck",
        "catering",
        "food"
    ]

    query_lower = query.lower()

    for word in keywords:

        if word in query_lower:

            result = food_df[
                food_df["business_type"]
                .str.contains(word, case=False, na=False)
            ]

            if not result.empty:
                return result

    return food_df.head(5)

# ==========================================
# SCHOLARSHIP SEARCH
# ==========================================

def search_scholarship(query):

    result = scholarship_df[
        scholarship_df["text"]
        .str.contains(query, case=False, na=False)
    ]

    if result.empty:
        return scholarship_df.head(5)

    return result.head(5)

# ==========================================
# SCHEME SEARCH
# ==========================================

def search_scheme(query):

    result = maharashtra_df[
        maharashtra_df["scheme_text"]
        .str.contains(query, case=False, na=False)
    ]

    if result.empty:
        return maharashtra_df.head(5)

    return result.head(5)

# ==========================================
# SCENARIO DETECTION
# ==========================================

def detect_scenario(query):

    query = query.lower()

    food_words = [
        "bakery",
        "food",
        "restaurant",
        "cafe",
        "fssai"
    ]

    scholarship_words = [
        "scholarship",
        "student",
        "college",
        "education",
        "engineering"
    ]

    if any(word in query for word in food_words):
        return "food"

    elif any(word in query for word in scholarship_words):
        return "scholarship"

    else:
        return "scheme"

# ==========================================
# AI RESPONSE
# ==========================================

def get_ai_response(query, data):

    model = genai.GenerativeModel(
        "gemini-2.5-flash"
    )

    prompt = f"""
You are GovGuide AI.

User Query:
{query}

Relevant Government Data:
{data}

Provide:

# Overview

# Required Documents

# Eligibility

# Step-by-Step Process

# Relevant Government Schemes

# Important Notes

Answer in clear markdown.
"""

    response = model.generate_content(prompt)

    return response.text

# ==========================================
# MAIN FUNCTION
# ==========================================

def navigate_query(query):

    scenario = detect_scenario(query)

    if scenario == "food":
        data = search_food(query)

    elif scenario == "scholarship":
        data = search_scholarship(query)

    else:
        data = search_scheme(query)

    return get_ai_response(
        query,
        data.to_string(index=False)
    )