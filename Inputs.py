## Incident report script
## rp = reporting person
rp_first_name = input("What is the victim's first name? ")
print("Hello" + rp_first_name + ", my name is Detective Good Guy, and I am here to help.")
print("I can't imagine " + rp_first_name + " how difficult this experience has been for you. I wish that none of this had happened to you. You don't deserve to be treated this way. I want to thank you for having the courage to share your story with me. I am going to do my best to help you get through this.")
print("First " + rp_first_name + ", I am going to need some help from you. I am going to ask you a series of questions about yourself and everyone involved in this incident; as well as the location of the incident and when it occurred. Once I have established those details, I want to hear your story about what happened. " + rp_first_name + ", can you help me with this?")
rp_last_name = input("What is your last name?")
print(rp_last_name + ", Is that correct?")
rp_home_address = input("What is your home address?")
print(rp_home_address + ", Is that correct?")
rp_phone_number = input("What is the best phone number to contact you at?")
print(rp_phone_number + ", Is that correct?")
## alt = alternate
rp_alt_phone_number = input("Is there another phone number that I should try if I can't reach you at your primary phone number?")
print(rp_alt_phone_number + ", Is that correct")
## DOB = date of birth
rp_DOB = input("What is your date of birth?")
print(rp_DOB + ", Is that correct?")
## SSID = Social Security ID number
rp_SSID = input("What is your social security ID number?")
print(rp_SSID + ", Is that correct?")
incident_location = input("Where did this occur?")
print(incident_location + ", Is that correct?")
## TDD_occurrence = time, day, date
TDD_occurrence = input("When did this happen?")
print(TDD_occurrence + ", Is that correct?")
suspect_name = input("What is the suspect's name?")
print(suspect_name + ", Is that correct?")
rp_narrative = input("Now please, " + rp_first_name + " Can you tell me what happened in your own words?")