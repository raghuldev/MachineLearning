# Create the base image
FROM python:3.7-slim

# Install Dependency
COPY ./requirements.txt /app/
RUN python -m pip install -r /app/requirements.txt

# Copy local folder into the container
COPY ./app.py /app/
COPY ./model_gender_scenario1_XGBoost.pkl /app/
COPY ./model_age_scenario1_XGBoost.pkl /app/
COPY ./test_data_scenario_1.csv /app/
COPY templates/ /app/templates/

# Change the working directory
WORKDIR /app/

# Set "python" as the entry point
ENTRYPOINT ["python"]

# Set the command as the script name
CMD ["app.py"]

#Expose the post 5000.
EXPOSE 5000
