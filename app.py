from flask import Flask, render_template
from coop import update_coop_data
from ica_maxi import update_maxi_data
from ica_supermarket import update_super_data
from willys import update_willys_data
#from coop import update_coop_data


 # Initializes the application 
app = Flask(__name__)

# Adds route
@app.route('/')
def home():
    
        update_willys_data()
        update_coop_data()
        update_maxi_data()
        update_super_data()
        
        return render_template("index.html")

# Runs the app
if __name__ == '__main__':
 app.run(debug=True)
