<img width="1536" height="1024" alt="ChatGPT Image Jun 5, 2026, 01_40_15 AM" src="https://github.com/user-attachments/assets/0135ea80-27af-4014-824a-2a41ae4e2fff" /># 🚀 Serverless File Sharing Portal

A secure, scalable, and fully serverless file-sharing platform built on AWS. Users can upload files, generate secure shareable links, and access files through shortened URLs without managing any backend servers.

This project demonstrates modern cloud-native architecture using AWS services including Lambda, API Gateway, S3, and DynamoDB.

---

## 🏗️ Architecture Diagram
<img width="1536" height="1024" alt="sharebuddy_flowdiagram" src="https://github.com/user-attachments/assets/6952dfa3-1fdf-4bc1-8a17-f5e2d56c2556" />


## 📌 Features

### Secure File Uploads

* Upload files directly to Amazon S3 using pre-signed URLs.
* No AWS credentials are exposed to the client.
* Eliminates the need for a traditional backend server.

### URL Shortening

* Automatically generates compact shareable links.
* Stores URL mappings in DynamoDB.
* Improves usability compared to long S3 pre-signed URLs.

### File Sharing

* Share uploaded files through generated links.
* One-click URL copy functionality.
* Easy distribution of files across devices and users.

### Fully Serverless Architecture

* No EC2 instances or server management.
* Event-driven AWS Lambda functions.
* Auto-scaling and pay-per-use pricing model.

### Metadata Management

* File and URL mapping information stored in DynamoDB.
* Fast lookup and retrieval of shared files.

### Security

* IAM-based access control.
* Time-limited pre-signed URLs.
* Private S3 bucket architecture.
* Least-privilege permissions for AWS services.

---

## 🏗️ Architecture

User → Frontend → API Gateway → AWS Lambda → DynamoDB

User → Frontend → S3 (via Pre-Signed URL)

Short URL Request → API Gateway → Lambda → DynamoDB → Original File URL

---

## ☁️ AWS Services Used

| Service            | Purpose                           |
| ------------------ | --------------------------------- |
| Amazon S3          | File storage                      |
| AWS Lambda         | Business logic and URL generation |
| Amazon API Gateway | REST API endpoints                |
| Amazon DynamoDB    | URL mapping and metadata storage  |
| AWS IAM            | Access control and security       |
| Amazon CloudWatch  | Monitoring and logging            |

---

## 🔄 Workflow

### Upload Process

1. User selects a file from the web application.
2. Frontend requests an upload URL from API Gateway.
3. Lambda generates a pre-signed S3 upload URL.
4. File is uploaded directly to S3.
5. Lambda creates a shortened URL entry in DynamoDB.
6. User receives a shareable short link.

### Download Process

1. User opens the short URL.
2. Lambda retrieves the original file information from DynamoDB.
3. A secure download URL is generated.
4. File is served directly from S3.

---

## 📂 Project Structure

```bash
serverless-file-sharing/
│
├── backend/
│   ├── generate_upload_url.py
│   ├── generate_download_url.py
│   ├── shorten_url.py
│   └── redirect_handler.py
│
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── app.js
│
├── screenshots/
│
└── README.md
```

---

## 🎯 Key Cloud Concepts Demonstrated

* Serverless Computing
* Event-Driven Architecture
* REST APIs
* Object Storage
* IAM Security
* URL Shortening Systems
* NoSQL Database Design
* Direct Browser-to-S3 Uploads
* Cloud Cost Optimization
* Scalable File Distribution

---

## 📸 Screenshots

### Upload Interface

(Add Screenshot Here)

### Generated Shareable Link

(Add Screenshot Here)

### Successful File Upload

(Add Screenshot Here)

---

## 🚀 Future Enhancements

* User Authentication with Amazon Cognito
* File Expiration Policies
* Download Analytics
* User Dashboard
* Multi-file Upload Support
* Custom Short URLs
* Password-Protected File Sharing
* Email Notifications

---

## 💡 Why This Project?

Traditional file-sharing applications require backend servers for handling uploads and downloads. This solution leverages AWS serverless services to remove server management overhead while maintaining security, scalability, and cost efficiency.

The architecture follows modern cloud-native design principles and demonstrates practical implementation of AWS services commonly used in production environments.

---

## 👨‍💻 Author

**Aditya Gaur**

* LinkedIn: https://www.linkedin.com/in/aditya-gaur005/
* Email: [aditya2405gaur@gmail.com](mailto:aditya2405gaur@gmail.com)

---

## 📄 License

This project is licensed under the MIT License.
