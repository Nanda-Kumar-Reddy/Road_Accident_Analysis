import streamlit as st
import pickle
import numpy as np
import pandas as pd

def load_model():
    with open('saved_steps.pkl','rb') as file:
        data=pickle.load(file)
    return data

data=load_model()

loaded_rf=data['model']

def show_predict_page():
    st.title("Road accident ananlysis")

    st.write(""" ### we need some data to predict""")

    Day_of_week={
        "Friday",
        "Thursday",
        "Wednesday",
        "Tuesday",
        "Monday",
        "Saturday",
        "Sunday",
    }

    Number_of_vehicles_involved={
        1,2,3,4,6,7,
    
    }

    Number_of_casualties={
        1,2,3,4,5,6,7,8, 
    }

    Area_accident_occured={
        "Office areas","Residential areas","Church areas","Industrial areas","School areas","Recreational areas","Outside rural areas",
        "Hospital areas","Market areas","Rural village areas","Rural village areasOffice areas","Recreational areas",
    }

    Types_of_Junction={
        "Y Shape","No junction","Crossing","O Shape","T Shape","X Shape",
    }

    Age_band_of_driver={
        "18-30","31-50","Over 51","Under 18",
    }

    Sex_of_driver={
        "Male","Female"
    }

    Educational_level={
        "Junior high school","Elementary school","High school","Above high school","Writing & reading","Illiterate"
    }   

    Vehicle_driver_relation={
        "Employee","Owner",
    }

    Type_of_vehicle={
        "Automobile","Lorry (41?100Q)","Pick up upto 10Q","Public (12 seats)","Stationwagen","Lorry (11?40Q)","Public (13?45 seats)",
        "Public (> 45 seats)","Long lorry","Taxi","Motorcycle","Special vehicle","Ridden horse","Turbo","Bajaj","Bicycle",
    }

    Driving_experience={
        "5-10yr","2-5yr","Above 10yr","1-2yr","Below 1yr","No Licence",
    }

    Service_year_of_vehicle={
        "2-5yrs","Above 10yr","5-10yrs","1-2yr","Below 1yr",
    }

    Type_of_collision={
        "Vehicle with vehicle collision","Collision with roadside objects","Collision with pedestrians","Rollover","Collision with animals",
        "Collision with roadside-parked vehicles","Fall from vehicles","With Train"
    }

    Sex_of_casualty={
        "Male","Female"
    }

    Age_band_of_casualty={
        "18-30","31-50","Under 18","Over 51","5",
    }

    Cause_of_accident={
        "No distancing","Getting off the vehicle improperly","Driving at high speed",
        "Changing lane to the right","Overturning",
        "Changing lane to the left","Turnover",
        "Driving carelessly","Overspeed",
        "No priority to vehicle","Overloading",
        "Moving Backward","Drunk driving",
        "No priority to pedestrian","Improper parking",
        "Overtaking","Driving under the influence of drugs","Driving to the left",
    }

    Hour_of_Day={
        1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,
    }

    Day_of_week1=st.selectbox("Day_of_week",Day_of_week)
    Number_of_vehicles_involved1=st.selectbox("Number of vehicles involved",Number_of_vehicles_involved)
    Number_of_casualties1=st.selectbox("Number_of_casualties",Number_of_casualties)
    Area_accident_occured1=st.selectbox("Area_accident_occured",Area_accident_occured)
    Types_of_Junction1=st.selectbox("Types_of_Junction",Types_of_Junction)
    Age_band_of_driver1=st.selectbox("Age_band_of_driver",Age_band_of_driver)
    Sex_of_driver1=st.selectbox("Sex_of_driver",Sex_of_driver)
    Educational_level1=st.selectbox("Educational_level",Educational_level)
    Vehicle_driver_relation1=st.selectbox("Vehicle_driver_relation",Vehicle_driver_relation)
    Type_of_vehicle1=st.selectbox("Type_of_vehicle",Type_of_vehicle)
    Driving_experience1=st.selectbox("Driving_experience",Driving_experience)
    Service_year_of_vehicle1=st.selectbox("Service_year_of_vehicle",Service_year_of_vehicle)
    Type_of_collision1=st.selectbox("Type_of_collision",Type_of_collision)
    Sex_of_casualty1=st.selectbox("Sex_of_casualty",Sex_of_casualty)
    Age_band_of_casualty1=st.selectbox("Age_band_of_casualty",Age_band_of_casualty)
    Cause_of_accident1=st.selectbox("Cause_of_accident",Cause_of_accident)
    Hour_of_Day1=st.selectbox("Hour_of_Day",Hour_of_Day)


    ok = st.button("predict severity")
    if(ok):
        my_dict = {
            "Day_of_week":Day_of_week1,
            "Number_of_vehicles_involved": Number_of_vehicles_involved1,
            "Number_of_casualties": Number_of_casualties1,
            "Area_accident_occured": Area_accident_occured1,
            "Types_of_Junction":Types_of_Junction1,
            "Age_band_of_driver":Age_band_of_driver1,
            "Sex_of_driver":Sex_of_driver1,
            "Educational_level":Educational_level1,
            "Vehicle_driver_relation":Vehicle_driver_relation1,
            "Type_of_vehicle":Type_of_vehicle1,
            "Driving_experience":Driving_experience1,
            "Service_year_of_vehicle":Service_year_of_vehicle1,
            "Type_of_collision":Type_of_collision1,
            "Sex_of_casualty":Sex_of_casualty1,
            "Age_band_of_casualty":Age_band_of_casualty1,
            "Cause_of_accident":Cause_of_accident1,
            "Hour_of_Day":Hour_of_Day1,
          }
        columns=['Number_of_vehicles_involved', 'Number_of_casualties', 'Hour_of_Day',
        'Day_of_week_Monday', 'Day_of_week_Saturday', 'Day_of_week_Sunday',
        'Area_accident_occured_  Recreational areas',
        'Area_accident_occured_ Hospital areas',
        'Area_accident_occured_ Outside rural areas',
        'Area_accident_occured_Recreational areas',
        'Area_accident_occured_Residential areas',
        'Area_accident_occured_Rural village areas',
        'Area_accident_occured_Rural village areasOffice areas',
        'Types_of_Junction_No junction', 'Types_of_Junction_Other',
        'Types_of_Junction_Unknown', 'Types_of_Junction_X Shape',
        'Age_band_of_driver_31-50', 'Age_band_of_driver_Over 51',
        'Age_band_of_driver_Under 18', 'Age_band_of_driver_Unknown',
        'Sex_of_driver_Unknown', 'Vehicle_driver_relation_Owner',
        'Type_of_vehicle_Long lorry', 'Type_of_vehicle_Lorry (11?40Q)',
        'Type_of_vehicle_Lorry (41?100Q)', 'Type_of_vehicle_Other',
        'Type_of_vehicle_Pick up upto 10Q',
        'Type_of_vehicle_Public (13?45 seats)',
        'Type_of_vehicle_Special vehicle', 'Driving_experience_2-5yr',
        'Driving_experience_Below 1yr', 'Driving_experience_No Licence',
        'Type_of_collision_Collision with pedestrians',
        'Type_of_collision_Unknown',
        'Type_of_collision_Vehicle with vehicle collision',
        'Sex_of_casualty_Male', 'Age_band_of_casualty_5',
        'Age_band_of_casualty_Over 51', 'Age_band_of_casualty_Under 18',
        'Cause_of_accident_Driving to the left',
        'Cause_of_accident_Improper parking',
        'Cause_of_accident_Moving Backward', 'Cause_of_accident_No distancing',
        'Cause_of_accident_No priority to pedestrian',
        'Cause_of_accident_No priority to vehicle',
        'Cause_of_accident_Overloading', 'Cause_of_accident_Overspeed',
        'Cause_of_accident_Overtaking', 'Cause_of_accident_Turnover']
        df = pd.DataFrame.from_dict([my_dict])
        df = pd.get_dummies(df).reindex(columns=columns, fill_value=0)
    
        predicted_value=loaded_rf.predict(df)
        if(predicted_value[0]==0):
            st.subheader(f"The severity of the accident is Fatal injury")
        if(predicted_value[0]==1):
            st.subheader(f"The severity of the accident is  Serious Injury")
        if(predicted_value[0]==2):
            st.subheader(f"The severity of the accident is  Slight Injury")
        