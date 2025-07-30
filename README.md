# Medical Chatbot Backend API 🏥🤖

A Django REST API backend for a medical chatbot system that provides AI-powered diabetes consultation, medical test analysis, and eye test processing using Google's Gemini AI model.

## 🌟 Features

### 🤖 AI-Powered Medical Chatbot
- **Conversational AI Doctor**: Specialized diabetes consultation chatbot
- **Language**: Responds in Arabic for better accessibility
- **Context-Aware**: Maintains conversation history and context
- **PDF Knowledge Base**: Uses diabetes.pdf as knowledge source via RAG (Retrieval-Augmented Generation)
- **Smart Responses**: Provides summarized, accurate medical advice

### 🏥 Medical Test Analysis
- **Diabetes Risk Assessment**: Analyzes multiple health parameters
- **Comprehensive Health Factors**: Evaluates 17+ health indicators including:
  - Blood pressure, cholesterol, BMI
  - Lifestyle factors (smoking, physical activity, diet)
  - Medical history (stroke, heart disease)
  - Demographics (age, gender, education, income)

### 👁️ Eye Test Processing
- **Image Analysis**: AI-powered eye test image processing
- **Automated Scoring**: Returns confidence scores for eye conditions
- **Secure Upload**: Image storage and processing pipeline

### 🔐 User Management
- **Custom User Model**: Email-based authentication
- **Token Authentication**: Secure API access
- **Permission Control**: Role-based access control

### 💬 Chat System
- **Multi-Chat Support**: Users can have multiple chat sessions
- **Message History**: Persistent conversation storage
- **Real-time Context**: Chat history integration with AI responses

## 🛠️ Technology Stack

- **Backend Framework**: Django 4.2.15 + Django REST Framework
- **AI/ML**: 
  - Google Gemini 1.5 Flash (LangChain integration)
  - FAISS vector database for document retrieval
  - LangChain for RAG implementation
- **Database**: SQLite (development) / PostgreSQL (production ready)
- **Authentication**: Token-based authentication
- **Documentation**: Swagger/OpenAPI with drf-yasg
- **File Processing**: Pillow for image handling, PyPDF for document processing

## 📋 API Endpoints

### Authentication
- `POST /api/users/` - User registration
- `POST /api/users/login/` - User login
- `GET /api/users/profile/` - Get user profile

### Chat System
- `GET /api/chat/` - List user chats
- `POST /api/chat/` - Create new chat
- `GET /api/chat/{id}/` - Get specific chat details

### Messaging
- `POST /api/message/` - Send message to chatbot
- `GET /api/message/` - Get message history

### Medical Tests
- `POST /api/medical_test/` - Submit diabetes risk assessment
- `GET /api/medical_test/` - Get user's medical test results

### Eye Tests
- `POST /api/eye_test/` - Upload eye test image for analysis
- `GET /api/eye_test/` - Get user's eye test results

### Documentation
- `GET /api/swagger/` - API documentation

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- Google API Key for Gemini AI
- Git

### 1. Clone the Repository
```bash
git clone <repository-url>
cd chatbot-backend
```

### 2. Create Virtual Environment
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Setup
Copy the environment template and configure your settings:
```bash
cp env_template.txt .env
```

The `.env` file should contain:
```env
# Django Configuration
SECRET_KEY=django-insecure-5*x=eaxv&!f=*n@g1&aul80^u=y^$f4gts0%fxaxqa9$y&!tvr
DEBUG=True

# Google AI Configuration
GOOGLE_API_KEY=AIzaSyD4MUKPfo5cixAk1AvGLC7PmgUPYBG7WHg

# CORS Configuration
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
```

**Note**: The Google API key included is from the development environment. For production, use your own API key.

### 5. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### 7. Run Development Server
```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

## 📊 Database Schema

The project includes a visual database schema:

![Database Schema](db_schema.png)

### Key Models:
- **User**: Custom user model with email authentication
- **Chat**: Chat sessions for organizing conversations
- **Message**: Individual messages with AI responses
- **Medical**: Diabetes risk assessment data
- **Test**: Eye test images and analysis results

## 🧪 Test Images

The project includes sample test images in the `test images/` directory for testing the eye test functionality:

- `image_png_*.png`: Sample eye test images for AI analysis
- `db_schema.png`: Database relationship diagram
- `لقطة_الشاشة_2024-11-27_064801.jpg`: Arabic interface screenshot

## 🤖 How the AI Model Works

### 1. **LangChain RAG Implementation**
```python
# Document Processing
loader = PyPDFLoader("message/diabetes.pdf")
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(documents)

# Vector Database
embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
vector = FAISS.from_documents(documents, embeddings)

# Retrieval Chain
retriever = vector.as_retriever()
retriever_chain = create_retrieval_chain(retriever, document_chain)
```

### 2. **Conversation Flow**
1. User sends message through API
2. System retrieves conversation history
3. LangChain processes query against diabetes knowledge base
4. Gemini AI generates contextually appropriate response
5. Response saved to database and returned to user

### 3. **AI Prompt Engineering**
The chatbot is configured as a diabetes specialist doctor with:
- Arabic language responses
- Patient-specific context (Male, 30 years old)
- Integration with medical test results
- Conversation memory for context retention

### 4. **Medical Test Integration**
- Eye test images are processed by AI model (placeholder function)
- Diabetes risk factors are collected via structured form
- Test results are incorporated into chatbot responses
- Users are guided to upload tests when relevant

## 🔧 Configuration

### Key Settings in `settings.py`:
- **CORS**: Configured for frontend integration
- **Authentication**: Token-based with custom user model
- **Media Files**: Configured for image uploads
- **REST Framework**: API configuration with authentication classes

### API Rate Limiting:
The Google Gemini API has built-in rate limiting with:
- Temperature: 0.7 (balanced creativity)
- Max retries: 2
- Timeout handling

## 🎯 Usage Examples

### 1. Register a User
```bash
curl -X POST http://127.0.0.1:8000/api/users/ \
  -H "Content-Type: application/json" \
  -d '{"email": "user@example.com", "password": "password123", "first_name": "John", "last_name": "Doe"}'
```

### 2. Send Message to Chatbot
```bash
curl -X POST http://127.0.0.1:8000/api/message/ \
  -H "Authorization: Token your_token_here" \
  -H "Content-Type: application/json" \
  -d '{"question": "ما هي أعراض السكري؟", "chat": 1}'
```

### 3. Upload Eye Test
```bash
curl -X POST http://127.0.0.1:8000/api/eye_test/ \
  -H "Authorization: Token your_token_here" \
  -F "attachment=@test_image.png"
```

## 📱 Frontend Integration

The API is designed to work with a React frontend (configured CORS for `localhost:5173`). Key integration points:

- **Authentication**: Token-based authentication
- **File Uploads**: Multipart form data for images
- **Real-time Chat**: RESTful API for message exchange
- **Test Results**: Structured data for medical assessments

## 🔒 Security Features

- **Token Authentication**: Secure API access
- **CORS Protection**: Configured allowed origins
- **Input Validation**: Django serializers for data validation
- **Permission Classes**: Role-based access control
- **File Upload Security**: Image validation and secure storage

## 🐛 Troubleshooting

### Common Issues:

1. **Google API Key Error**
   - Ensure `GOOGLE_API_KEY` is set in environment
   - Verify API key has Gemini access permissions

2. **Database Migration Issues**
   ```bash
   python manage.py makemigrations --empty appname
   python manage.py migrate --fake-initial
   ```

3. **CORS Issues**
   - Check `CORS_ALLOWED_ORIGINS` in settings
   - Verify frontend URL matches configuration

4. **File Upload Issues**
   - Ensure media directories exist
   - Check file permissions on upload directory

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For questions or support, please create an issue in the repository or contact the development team.

---

**Note**: This is a medical information system. Responses are for educational purposes only and should not replace professional medical advice.