import pandas as pd

# Load the dataset
file_path = 'D:\Python Hotel Booking Analysis\hotel_booking.csv'
hotel_data = pd.read_csv(file_path)

# Display the first few rows of the dataset
hotel_data.head()
# Data Summary
data_summary = {
    "Shape": hotel_data.shape,
    "Data Types": hotel_data.dtypes,
    "Missing Values": hotel_data.isnull().sum()
}

data_summary
# Descriptive statistics for numerical columns
numerical_stats = hotel_data.describe()

# Descriptive statistics for categorical columns
categorical_stats = hotel_data.describe(include=['object'])

numerical_stats, categorical_stats
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style of the visualization
sns.set(style="whitegrid")

# Distribution of lead time
plt.figure(figsize=(10, 6))
sns.histplot(hotel_data['lead_time'], bins=50, kde=True)
plt.title('Distribution of Lead Time')
plt.xlabel('Lead Time (days)')
plt.ylabel('Frequency')
plt.show()

# Distribution of ADR
plt.figure(figsize=(10, 6))
sns.histplot(hotel_data['adr'], bins=50, kde=True)
plt.title('Distribution of Average Daily Rate (ADR)')
plt.xlabel('ADR')
plt.ylabel('Frequency')
plt.show()

# Distribution of stays in weekend nights
plt.figure(figsize=(10, 6))
sns.histplot(hotel_data['stays_in_weekend_nights'], bins=20, kde=True)
plt.title('Distribution of Stays in Weekend Nights')
plt.xlabel('Stays in Weekend Nights')
plt.ylabel('Frequency')
plt.show()

# Distribution of stays in week nights
plt.figure(figsize=(10, 6))
sns.histplot(hotel_data['stays_in_week_nights'], bins=20, kde=True)
plt.title('Distribution of Stays in Week Nights')
plt.xlabel('Stays in Week Nights')
plt.ylabel('Frequency')
plt.show()

# Count plot of hotel types
plt.figure(figsize=(10, 6))
sns.countplot(data=hotel_data, x='hotel')
plt.title('Count of Hotel Types')
plt.xlabel('Hotel Type')
plt.ylabel('Count')
plt.show()

# Count plot of reservation status
plt.figure(figsize=(10, 6))
sns.countplot(data=hotel_data, x='reservation_status')
plt.title('Count of Reservation Status')
plt.xlabel('Reservation Status')
plt.ylabel('Count')
plt.show()
