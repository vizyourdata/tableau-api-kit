# Tableau API Kit  
Your ultimate starter guide to mastering all of Tableau’s APIs — from REST to JavaScript, Metadata, Hyper, Document API, and more. Automate, integrate, and optimize your Tableau workflows with ease.

---

## 🚀 About This Repository  
**`tableau-api-kit`** is designed to help developers, data analysts, and Tableau enthusiasts quickly get started with Tableau’s APIs. Whether you’re a Python user automating tasks with the REST API, embedding dashboards with JavaScript, or managing metadata efficiently, this repo has you covered.

### Features:
- Starter scripts and examples for each Tableau API.
- Practical use cases with detailed explanations.
- Ready-to-run code snippets to save you time.
- Links to official Tableau documentation for deeper exploration.

---

## 📚 Included APIs  
### 1. **Tableau REST API**
Automate common administrative tasks such as user management, content publishing, and view history extraction.  
- Example: Pull all users and export to Excel.  
- File: `rest_api/get_users.py`  

### 2. **Tableau JavaScript API (Embedding API)**  
Embed and interact with Tableau dashboards in your web applications.  
- Example: Dynamic parameter selection on embedded dashboards.  
- File: `javascript_api/embedded_dashboard.html`  


### 3. **Tableau Metadata API**  
Access detailed insights about your Tableau Server environment and lineage.  
- Example: Query upstream and downstream dependencies.  
- File: `metadata_api/query_dependencies.py`  

### 4. **Tableau Hyper API**  
Create and manage `.hyper` files for efficient data extraction.  
- Example: Insert and query data from a `.hyper` file.  
- File: `hyper_api/create_hyper_file.py`  

### 5. **Tableau Document API**  
Programmatically modify Tableau Workbook XML files.  
- Example: Update default parameters in `.twb` files.  
- File: `document_api/update_parameters.py`  

---

## 🛠️ Prerequisites  
### Software Requirements:
- **Python**: Version 3.7+ (for REST, Metadata, Hyper, and Document APIs).  
- **Node.js**: For JavaScript API examples.  
- **Tableau Server**: Access to a server instance (or Tableau Cloud).  

### Install Dependencies:
Install the required Python packages:  
```bash
pip install tableauserverclient pandas tableauhyperapi
