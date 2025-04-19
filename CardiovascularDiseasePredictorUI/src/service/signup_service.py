
class SignupService:
    def signup():
        if request.method == "POST":
            new_first_name = request.form['firstName']
            new_last_name = request.form['lastName']
            new_company = request.form['company']
            new_username = request.form['username']
            new_password = request.form['password']

            # Push to Database
            try:
                query = insert(Profiler).values(firstname=new_first_name, lastname=new_last_name, company=new_company,
                                                username=new_username, password=new_password)
                insert_query(query)
                return render_template("index.html")
            except:
                return "There was an error adding the account."
        else:
            return render_template("signup.html")