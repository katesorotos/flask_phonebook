from flask import Flask, render_template, request
from test_phonebook_database import  search_by_person, search_by_business_cat, search_by_business_name  

app = Flask(__name__)


@app.route("/" , methods=['GET', 'POST'])
def home():
    if request.method=="GET":
        resp_person = None
        resp_bus_cat = None
        resp_bus_name = None
        return render_template('template.html', resp_person=resp_person, resp_bus_cat=resp_bus_cat, resp_bus_name=resp_bus_name)
        
    elif request.method == "POST":
        if 'person_location' in request.form:
            form_data = request.form
            user_location = form_data.get('person_location', "")
            person_name_search = form_data['person_name']
        
            resp_person = search_by_person(user_location, person_name_search)
            resp_bus_cat = None
            resp_bus_name = None
            return render_template('template.html',resp_person=resp_person, resp_bus_cat=resp_bus_cat, resp_bus_name=resp_bus_name, user_location=user_location, person_name_search=person_name_search)
        
        elif 'business_name' in request.form:

            
            form_data = request.form
            user_location = form_data.get('business_location', "")
            business_cat_search = form_data.get('business_type', "")
            
            business_name_search = form_data.get('business_name', "")
            
            if business_cat_search=="":
                resp_person = None
                resp_bus_cat = None
                print(business_name_search, user_location )
                resp_bus_name = search_by_business_name(business_name_search, user_location)
                print(resp_bus_name)
                return render_template('template.html',resp_person=resp_person, resp_bus_cat=resp_bus_cat, resp_bus_name=resp_bus_name,  user_location=user_location, business_name_search=business_name_search)
            
            else:
                resp_person = None
                resp_bus_cat = search_by_business_cat(business_cat_search, user_location)
                resp_bus_name = None
                return render_template('template.html',resp_person=resp_person, resp_bus_cat=resp_bus_cat, resp_bus_name=resp_bus_name,  user_location=user_location, business_cat_search=business_cat_search)
        
         
    else:
        return render_template("template.html", resp_person="No Response")
        
        

        

    
    
#@app.route("/about")
#def about():
#    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
