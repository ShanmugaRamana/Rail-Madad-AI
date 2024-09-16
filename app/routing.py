import random

def smart_routing(complaint_category):
    departments = {
        'Cleanliness': 'Sanitation Dept.',
        'Damage': 'Maintenance Dept.',
        'Staff Behaviour': 'Human Resources'
    }
    
    return departments.get(complaint_category, "General Enquiry")

def generate_response(complaint_id):
    responses = [
        "Thank you for your complaint. We are addressing it.",
        "Your complaint has been routed to the appropriate department."
    ]
    return random.choice(responses) + f" Your complaint ID is {complaint_id}."
