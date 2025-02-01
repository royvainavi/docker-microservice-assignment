## **📌 Docker Assignment - A1**
This project implements a **microservice architecture** using **Docker**. It consists of two containers (`app1` and `app2`) that communicate via a **Docker network** to process **JSON input**, validate files, and calculate sums from CSV data.

---

## **📖 How It Works**

### **🛠 Containers**
1️⃣ **`app1`**:
   - Listens on **port `6000`** for **HTTP POST requests**.  
   - Validates **JSON input** and checks if the file exists.  
   - Forwards **valid requests** to `app2` and returns the response.  

2️⃣ **`app2`**:
   - Mounts the **`data/` directory** to access CSV files.  
   - Processes CSV files, calculates **sums for the specified product**, and handles errors.  

---

## **📂 File Structure**
```
A1/
├── app1/
│   ├── app1.py
│   ├── Dockerfile
├── app2/
│   ├── app2.py
│   ├── Dockerfile
├── data/
│   ├── file.yml
│   ├── file2.yml
├── docker-compose.yaml
├── README.md
```

---

## **🚀 How to Run**
### **1️⃣ Build Docker Images**
```sh
# Build app1
cd app1
docker build -t <your-dockerhub-username>/app1 .

# Build app2
cd ../app2
docker build -t <your-dockerhub-username>/app2 .
```

### **2️⃣ Run with Docker Compose**
```sh
# From the root directory (where docker-compose.yaml is located)
docker-compose up
```

---

## **🧪 Testing**
### **1️⃣ Invalid JSON Input**
```sh
curl -X POST http://localhost:6000/calculate -H "Content-Type: application/json" -d '{"file": null}'
```
**Expected Response:**
```json
{
  "file": null,
  "error": "Invalid JSON input."
}
```

### **2️⃣ File Not Found**
```sh
curl -X POST http://localhost:6000/calculate -H "Content-Type: application/json" -d '{"file": "nonexistent.yml", "product": "wheat"}'
```
**Expected Response:**
```json
{
  "file": "nonexistent.yml",
  "error": "File not found."
}
```

### **3️⃣ Calculate Sum**
✅ Ensure `file.yml` exists in the `data` directory with this content:
```
product,amount
wheat,10
wheat,20
oats,5
```
Now, send:
```sh
curl -X POST http://localhost:6000/calculate -H "Content-Type: application/json" -d '{"file": "file.yml", "product": "wheat"}'
```
**Expected Response:**
```json
{
  "file": "file.yml",
  "sum": 30
}
```

### **4️⃣ Invalid CSV Format**
✅ Ensure `file2.yml` exists in `data/` with invalid content:
```
productamount
wheat10
```
Now, send:
```sh
curl -X POST http://localhost:6000/calculate -H "Content-Type: application/json" -d '{"file": "file2.yml", "product": "wheat"}'
```
**Expected Response:**
```json
{
  "file": "file2.yml",
  "error": "Input file not in CSV format."
}
```

---

## **🛠 Troubleshooting**
- **Check Logs**:
  ```sh
  docker-compose logs app1  # View logs for app1
  docker-compose logs app2  # View logs for app2
  ```
- **Verify DockerHub Images**:
  Ensure `docker-compose.yaml` references your DockerHub images (not local builds).

---

## **👤 Author**
- **Name**: Vainavi Roy  
- **Banner ID**: B00881261  
- **CSID**: vroy  

---

