def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

    


print_kwargs(name="superman", power='laser')
print_kwargs(name="superman")
print_kwargs(name="superman", power='laser', enemy ="cak")