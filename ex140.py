def postal_reader(post):
    province = ''
    area_type = ''
    province_dict = {'A': 'Newfoundland', 'B':'Nova Scotia', 'C':'Prince Edward Island','E':'New Brunswick', 'G':'Quebec','H':'Quebec','J':'Quebec', 'KLMNP':'Ontario','L':'Ontario','M':'Ontario','N':'Ontario','P':'Ontario', 'R':'Manitoba', 'S':'Saskatchewan', 'T':'Alberta', 'V':'British Columbia','X':'Nunavut or Northwest Territories', 'Y':'Yukon'}

    post = post.replace(" ", "")
    province = province_dict[post[0]]
    if post[1] == 0:
        area_type = "rural"
    else:
        area_type = "urban"
    
    return f"Your province is {province} and your area type is {area_type}"

input_text = input('please type in a valid postal code')
print(postal_reader(input_text))