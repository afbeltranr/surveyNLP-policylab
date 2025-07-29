"""Topic label mapping and utilities."""

TOPIC_LABELS = {
    0: "Healthcare: Medication Access",
    1: "Healthcare: Service Delays",
    2: "Community: Institutional Trust",
    3: "Social: Youth Migration",
    4: "Infrastructure: Housing",
    5: "Economy: Informal Sector",
    6: "Governance: Institutional Trust",
    7: "Infrastructure: Power Supply",
    8: "Services: Waste Management",
    9: "Infrastructure: Water Access",
    10: "Social: Community Participation",
    11: "Healthcare: Mental Health",
    12: "Economy: Entrepreneurship",
    13: "Economy: Local Employment",
    14: "Healthcare: Medical Facilities",
    15: "Governance: Civic Engagement",
    16: "Services: Water Quality",
    17: "Governance: Response Time",
    18: "Governance: Public Communication"
}

# Group topics by main category
TOPIC_CATEGORIES = {
    "Healthcare": [0, 1, 11, 14],
    "Infrastructure": [4, 7, 9, 16],
    "Economy": [5, 12, 13],
    "Social": [3, 10],
    "Governance": [2, 6, 15, 17, 18],
    "Services": [8]
}

def get_topic_label(topic_id):
    """Get the human-readable label for a topic ID."""
    return TOPIC_LABELS.get(topic_id, f"Topic {topic_id}")

def get_topic_category(topic_id):
    """Get the main category for a topic ID."""
    for category, topics in TOPIC_CATEGORIES.items():
        if topic_id in topics:
            return category
    return "Other"

def get_category_color(category):
    """Get a consistent color for each main category."""
    color_map = {
        "Healthcare": "#FF9999",
        "Infrastructure": "#66B2FF",
        "Economy": "#99FF99",
        "Social": "#FFCC99",
        "Governance": "#FF99FF",
        "Services": "#FFFF99",
        "Other": "#CCCCCC"
    }
    return color_map.get(category, "#CCCCCC")
