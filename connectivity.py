def is_connectivity_issue(prompt): # Function is meant to determine if user prompt suggests an issue related with connectivity.
    keywords = ['disconnect', 'can\'t connect', 'connection lost', 'network issue', 'connectivity', 'connect', 'connection', 'disconnected', 'disconnects']
    # The assumption is made that users will use cartain dictionary to decribe the problem.
    # If these keywords are used, there is a high chance that user has a connectivity issue.
    # The keywords might be altered.
    
    return any((keyword in prompt.lower() for keyword in keywords))

def is_device(prompt):# Function checks if the user specified their device in the initial prompt to avoid the chatbot asking for the information the user already provided. 
    keywords = ['phone', 'android', 'iphone', 'computer', 'laptop', 'kindle', 'nintendo', 'switch', 'playstation', 'xbox', 'rasberry', 'chromebook', 'tv']
    # In this function only the most popular itemsare listed thus it does not cover all of the possible cases. 
    
    return any((keyword in prompt.lower() for keyword in keywords))

def has_country(prompt):# Function checks if the user specified their location in the initial prompt to avoid the chatbot asking for the information the user already provided. 
    countries = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", 
    "Antigua and Barbuda", "Argentina", "Armenia", "Australia", 
    "Austria", "Azerbaijan", "The Bahamas", "Bahrain", "Bangladesh", 
    "Barbados", "Belarus", "Belgium", "Belize", "Benin", 
    "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", 
    "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", 
    "Cabo Verde", "Cambodia", "Cameroon", "Canada", 
    "Central African Republic", "Chad", "Chile", "China", 
    "Colombia", "Comoros", "Congo, Democratic Republic of the", 
    "Congo, Republic of the", "Costa Rica", 
    "Croatia", "Cuba", "Cyprus", "Czech", "Denmark", 
    "Djibouti", "Dominica", "Dominican Republic", 
    "Timor", "Ecuador", "Egypt", 
    "Salvador", "Eritrea", "Estonia", 
    "Eswatini", "Ethiopia", "Fiji", "Finland", "France", 
    "Gabon", "The Gambia", "Georgia", "Germany", "Ghana", 
    "Greece", "Grenada", "Guatemala", "Guinea", 
    "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", 
    "India", "Indonesia", "Iran", "Iraq", "Ireland", 
    "Israel", "Italy", "Jamaica", "Japan", "Jordan", 
    "Kazakhstan", "Kenya", "Kiribati", "Korea, North", 
    "Korea, South", "Kosovo", "Kuwait", "Kyrgyzstan", 
    "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", 
    "Libya", "Liechtenstein", "Lithuania", "Luxembourg", 
    "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", 
    "Malta", "Marshall", "Mauritania", "Mauritius", 
    "Mexico", "Micronesia, Federated States of", "Moldova", 
    "Monaco", "Mongolia", "Montenegro", "Morocco", 
    "Mozambique", "Myanmar", "Burma", "Namibia", "Nauru", 
    "Nepal", "Netherlands", "New Zealand", "Nicaragua", 
    "Niger", "Nigeria", "North Macedonia", "Norway", "Oman", 
    "Pakistan", "Palau", "Panama", "Papua New Guinea", 
    "Paraguay", "Peru", "Philippines", "Poland", "Portugal", 
    "Qatar", "Romania", "Russia", "Rwanda", 
    "Saint Kitts and Nevis", "Saint Lucia", 
    "Saint Vincent and the Grenadines", "Samoa", "San Marino", 
    "Sao Tome and Principe", "Saudi Arabia", "Senegal", 
    "Serbia", "Seychelles", "Sierra Leone", "Singapore", 
    "Slovakia", "Slovenia", "Solomon Islands", "Somalia", 
    "South Africa", "Spain", "Sri Lanka", "Sudan", 
    "Sudan, South", "Suriname", "Sweden", "Switzerland", 
    "Syria", "Taiwan", "Tajikistan", "Tanzania", 
    "Thailand", "Togo", "Tonga", "Trinidad and Tobago", 
    "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", 
    "Uganda", "Ukraine", "United Arab Emirates", 
    "United Kingdom", "United States", "Uruguay", "England",
    "Uzbekistan", "Vanuatu", "Vatican", "Venezuela", 
    "Vietnam", "Yemen", "Zambia", "Zimbabwe", "US", "UK", "America"
    ]
    # This function only checks for the country, thus if the user provides their nationality or a city it will not work.

    return any((keyword.lower() in prompt.lower() for keyword in countries))

def is_OS(prompt):# Function checks if the user specified their OS in the initial prompt to avoid the chatbot asking for the information the user already provided. 
    keywords = [' microsoft', 'windows', 'mac', 'android', 'linux', 'ubuntu', 'fedora', 'iphone', 'ios']
    # In this function only the most popular OS are listed thus it does not cover all of the possible cases. 
    
    return any((keyword.lower() in prompt.lower() for keyword in keywords))