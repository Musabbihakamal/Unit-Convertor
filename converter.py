import streamlit as st

#title of the app
st.title("UNIT CONVERTER APP")

#let the user pick what they want to convert
category = st.selectbox("CHOOSE WHAT TO CONVERT:" , ["LENGTH" , "TEMPERATURE"])

#take input from the user
value = st.number_input("ENTER THE VALUE TO CONVERT:" , value=0.0)

#lenght conversion
if category == "LENGTH":
    st.subheader("LENGTH CONVERTER")

    #length unit
    length_unit =["METERS" , "KILOMETERS"  , "MILES"]

    #ask from value and convert it into to value
    from_unit = st.selectbox("FROM UNIT:" , length_unit)
    to_unit =st.selectbox("TO UNIT:" , length_unit)

elif category == "TEMPERATURE":
   st.subheader("TEMPERATURE CONVERTER")          

   #temperature unit
   temperature_unit =["CELCIUS" , "KELVIN" , "FAHRENHEIT"]

   #ask value and convert into other value
   from_unit = st.selectbox("FROM UNIT" ,temperature_unit)
   to_unit= st.selectbox("TO UNIT" , temperature_unit)

    
def convert_unit(value, from_unit, to_unit):
   if category == "LENGTH":
      if from_unit == "METERS":
         if to_unit == "METERS":
             return value
         elif to_unit == "KILOMETERS":
             return value/1000
         elif to_unit == "MILES":
               return value/1609.34
            
      elif from_unit == "KILOMETERS":
         if to_unit == "KILOMETERS":
              return value
         elif to_unit == "METERS":
              return value*1000
         elif to_unit == "MILES":
              return value/0.6213762
           
      elif from_unit == "MILES":
         if to_unit == "METERS":
              return value*1609.34
         elif to_unit == "MILES":
              return value
         elif to_unit == "KILOMETER":
              return value*0.6213762     

   elif category == "TEMPERATURE":
       if from_unit == "CELCIUS":
         if to_unit == "CELCIUS":
            return value
         elif to_unit == "FAHRENHEIT":
            return (value*9/5)+32
         elif to_unit == "KELVIN":
           return value+273

       elif from_unit =="FAHRENHEIT":
          if to_unit == "FAHRENHEIT" :
            return value
          elif to_unit == "CELCIUS":
            return (value-32)*5/9
          elif to_unit == "KELVIN":
            return ((value - 32) * 5/9) + 273.15
         
       elif from_unit == "KELVIN":
         if to_unit == "KELVIN":
            return value 
         elif to_unit == "CELCIUS":
            return value-273
         elif to_unit == "FAHRENHEIT":
            return ((value - 273.15) * 9/5) + 32

if st.button("CONVERT"):
   result =convert_unit(value,from_unit ,to_unit)
   st.success(f"The Result is {result:.2f}")
