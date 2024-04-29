import pandas as pd
from faker import Faker

fake = Faker()


def generate_user_data(num_entries):
    user_data = []
    for _ in range(num_entries):
        user_id = fake.random_int(min=1, max=1000)
        user_name = fake.name()
        user_address = fake.address()
        user_phone = fake.phone_number()

        user_data.append([user_name, user_id, user_address,user_phone])
    return user_data


if __name__ == "__main__":

    user_data = generate_user_data(100)
    users_df = pd.DataFrame(user_data, columns=['user_name', 'user_id', 'user_address','user_phone'])

    users_df.to_parquet('users.parquet', index=False)
