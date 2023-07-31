echo "Downloading depedencies"
pip install --target ./package -r requirements.txt
echo "Packaging lambda"
cd package
zip -r ../deployment.zip .
cd ..
zip -r deployment.zip ./clients ./templates ./utilities lambda_function.py transactions.csv
