import streamlit as st
import pandas as pd
import joblib

def app():
    model=joblib.load('model.h5')
    st.header("Used Cars Prediction")
    st.write("This project predicts used cars price based on saome features")
    Body=st.radio('Select Body Type',['Sedan','Hatchback','SUV'])
    Fuel=st.radio('Select Fuel Type',['Benzine','Natural,Gas'])
    Kilometers=st.radio('Select Kilometers of Car ',['140000 to 159999','180000 to 199999','10000 to 19999','More than 200000','90000 to 99999','100000 to 119999','160000 to 179999','120000 to 139999','0 to 9999','20000 to 29999','30000 to 39999','80000 to 89999','60000 to 69999' ,'70000 to 79999','40000 to 49999','50000 to 59999'])
    Engine=st.radio('Select Engine Type',['1600 CC','1000 - 1300 CC','1400 - 1500 CC'])
    Transmission=st.radio('Select Transmission Type',['Automatic','Manual'])
    car_age=st.number_input('Select Car Age',value=0)
    carModelBrand=st.radio('Select Car Model',['Hyundai Accent','Hyundai Avante','Hyundai I10','Hyundai Elantra','Hyundai Excel','Hyundai Matrix','Hyundai Tucson','Hyundai Verna','Chevrolet Cruze','Chevrolet Aveo','Chevrolet Lanos','Chevrolet Optra','Fiat 128','Fiat 131','Fiat Punto','Fiat Shahin','Fiat Tipo','Fiat Uno'])
    Predict = st.button("Predict")
    if Transmission == 'Automatic':
        Transmission=1
    else :
        Transmission=0
    if Fuel == 'Benzine':
        Fuel=0
    else :
        Fuel=1
    if Body == 'Sedan':
        Body=0
    elif Body == 'Hatchback' :
        Body=1
    else:
        Body=2
    if Kilometers == '140000 to 159999':
        Kilometers=159999
    elif  Kilometers ==  '180000 to 199999':
        Kilometers=199999 
    elif Kilometers == '10000 to 19999':
        Kilometers=19999
    elif Kilometers == 'More than 200000':
        Kilometers=200000
    elif Kilometers =='90000 to 99999':
        Kilometers=99999 
    elif Kilometers == '100000 to 119999':
        Kilometers=19999 
    elif Kilometers =='160000 to 179999':
        Kilometers=179999
    elif Kilometers =='120000 to 139999':
        Kilometers=139999
    elif Kilometers =='0 to 9999':
        Kilometers=9999
    elif Kilometers == '20000 to 29999':
        Kilometers=29999
    elif Kilometers == '30000 to 39999':
        Kilometers=39999
    elif Kilometers == '80000 to 89999':
        Kilometers=89999
    elif Kilometers =='60000 to 69999':
        Kilometers=69999
    elif Kilometers =='70000 to 79999':
        Kilometers=79999
    elif Kilometers == '40000 to 49999':
        Kilometers=49999
    else:
        Kilometers=59999
    if carModelBrand == 'Hyundai Accent':
        carModelBrand =0
    elif carModelBrand == 'Hyundai Avante':
        carModelBrand =1
    elif carModelBrand =='Hyundai I10':
        carModelBrand =2
    elif carModelBrand =='Hyundai Elantra':
        carModelBrand =3
    elif carModelBrand =='Hyundai Excel':
        carModelBrand =4
    elif carModelBrand =='Hyundai Matrix':
        carModelBrand =5
    elif carModelBrand =='Hyundai Tucson':
        carModelBrand =6
    elif carModelBrand =='Hyundai Verna':
        carModelBrand =7
    elif carModelBrand =='Chevrolet Cruze':
        carModelBrand =7
    elif carModelBrand =='Chevrolet Aveo':
        carModelBrand =8
    elif carModelBrand =='Chevrolet Lanos':
        carModelBrand =9
    elif carModelBrand =='Chevrolet Optra':
        carModelBrand =10
    elif carModelBrand =='Fiat 128':
        carModelBrand =11
    elif carModelBrand =='Fiat 131':
        carModelBrand =12
    elif carModelBrand =='Fiat Punto':
        carModelBrand =13
    elif carModelBrand =='Fiat Shahin':
        carModelBrand =14
    elif carModelBrand =='Fiat Tipo':
        carModelBrand =15
    else:
        carModelBrand =16
    if Engine == '1600 CC':
        Engine=1600
    elif Engine == '1000 - 1300 CC':
        Engine=1300
    else:
        Engine=1500
    if Predict:
        df=pd.DataFrame.from_dict(
            {
                "Body" : [Body],
                "Fuel" : [Fuel] ,
                "Kilometers":[Kilometers],
                "Engine":[Engine] ,
                "Transmission":[Transmission],
                "carModelBrand":[carModelBrand],
                "car_age":[car_age]

                }
                )
        st.write("Input Data: ")
        st.dataframe(df)
        pred = model.predict(df)
        st.write(F"Prediction: {pred}")

app()