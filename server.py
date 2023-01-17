import streamlit as st 
#from flask import Flask
import pickle


#app = Flask(__name__)
print('Successfully executed ')

model = pickle.load(open('model.pkl', 'rb'))
# labels ={
#   0: "setosa",
#   1: "versicolor",
#   2: "virginica"
# }

#@app.route('/')
# def welcome():
#     return "Index Page"

#@app.route('/predict',methods=['POST'])
def predict(sl,sw,pl,pw):
    prediction=model.predict([[sl,sw,pl,pw]])
    return prediction
    #[prediction[0]]
def main():
    st.title("IRIS Prediction")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit IRIS Predictor </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    sl = st.text_input("Sepal Length","Type Here")
    sw = st.text_input("Sepal Width","Type Here")
    pl = st.text_input("Petal Length","Type Here")
    pw = st.text_input("Petal Width","Type Here")
    result=""
    if st.button("Predict"):
        result=predict(sl,sw,pl,pw)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

#if __name__=='__main__':
main()
