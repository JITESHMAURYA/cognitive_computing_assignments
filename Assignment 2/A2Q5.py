sample_dict={
    "name": "kelly",
    "age":25,
    "salary":8000,
    "city":"New York"
}
x=sample_dict["city"]
sample_dict.pop("city")
sample_dict["location"]=x
print(sample_dict)