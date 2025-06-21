import json
import re
from datetime import datetime

class StudentChatbot:
    def __init__(self):
        # Load the knowledge base
        self.knowledge_base = {
            "program_name": "الهندسة الكهربية والحاسبات",
            "program_code": "ECE-C",
            "university": "جامعة المنوفية",
            "faculty": "كلية الهندسة",
            "degree_awarded": "بكالوريوس في الهندسة",
            "study_system": "نظام الساعات المعتمدة",
            "total_required_credits": 180,
            "program_duration": "عشر فصول دراسية كحد أقصى",
            "admission_requirements": [
                "الحصول على شهادة الثانوية العامة - شعبة رياضيات",
                "أو ما يعادلها حسب تنسيق الجامعات"
            ],
            "total_credits": 180,
            "requirements": {
                "university": 25,
                "faculty": 45,
                "specialization": 110
            },
            "registration": {
                "eligibility": "شهادة الثانوية العامة شعبة الرياضيات أو ما يعادلها",
                "max_duration": "10 سنوات (10 فصول دراسية رئيسية)",
                "min_duration": "9 فصول دراسية رئيسية",
                "max_credits_per_semester": {
                    "GPA_above_3": 21,
                    "GPA_above_2": 18,
                    "GPA_below_2": 14
                },
                "summer_max_credits": 6
            },
            "graduation_requirements": {
                "minimum_gpa": 2.00,
                "honors_requirements": {
                    "minimum_gpa": 3.3,
                    "no_F_grades": True
                },
                "project_requirement": "تنفيذ مشروع تخرج خلال فصلين دراسيين",
                "internship": "تدريب ميداني لمدة لا تقل عن 8 أسابيع",
                "credit_hours": {
                    "university_requirements": 25,
                    "faculty_requirements": 45,
                    "specialization_requirements": 110
                }
            },
            "grading_scale": {
                "A+": "4.00 (97% فما فوق)",
                "A": "4.00 (93%-96%)",
                "A-": "3.70 (89%-92%)",
                "B+": "3.30 (84%-88%)",
                "B": "3.00 (80%-83%)",
                "B-": "2.70 (76%-79%)",
                "C+": "2.30 (73%-75%)",
                "C": "2.00 (70%-72%)",
                "D": "1.00 (60%-64%)",
                "F": "0.00 (أقل من 60%)"
            },
            "language_of_instruction": "اللغة الإنجليزية",
            "semesters": {
                "fall": "يبدأ في سبتمبر",
                "spring": "يبدأ في فبراير",
                "summer": "اختياري، يبدأ في يوليو"
            },
            "courses": {
                "university_requirements": [
                    {"code": "GEN-C001", "name": "English Language", "credits": 3},
                    {"code": "GEN-C002", "name": "Introduction to Computers", "credits": 3},
                    {"code": "GEN-C101", "name": "Human Rights", "credits": 2},
                    {"code": "GEN-C102", "name": "Project Management", "credits": 2},
                    {"code": "GEN-C201", "name": "Presentation Skills", "credits": 3},
                    {"code": "GEN-C202", "name": "Foundation of Economics", "credits": 3},
                    {"code": "GEN-C301", "name": "Writing Technical Report", "credits": 3}
                ],
                "electrical_engineering_core": [
                    {"code": "ELE-C101", "name": "Circuits (1)", "credits": 3},
                    {"code": "ECE-C101", "name": "Digital Logic", "credits": 3},
                    {"code": "ELE-C102", "name": "Circuits (2)", "credits": 3},
                    {"code": "ELE-C201", "name": "Electromagnetic Fields", "credits": 3},
                    {"code": "ELE-C301", "name": "Control Systems", "credits": 3},
                    {"code": "ELE-C401", "name": "Electrical Machines", "credits": 3},
                    {"code": "ELE-C501", "name": "Power Systems", "credits": 3}
                ]
            },
            "policies": {
                "attendance": "الحضور الإلزامي 75% على الأقل لدخول الامتحان",
                "academic_warning": "إنذار أكاديمي إذا كان المعدل التراكمي أقل من 2.0",
                "course_repeat": "يمكن إعادة المقرر لتحسين المعدل (بحد أقصى 5 مقررات)",
                "withdrawal": "الانسحاب مسموح خلال 8 أسابيع في الفصول الرئيسية/4 أسابيع في الصيفي"
            },
            "student_services": {
                "academic_advisor": "يتم تعيين مرشد أكاديمي لكل طالب عند الالتحاق",
                "industrial_training": {
                    "requirement": "8 أسابيع تدريب بعد إكمال 120 ساعة معتمدة",
                    "credits": 2
                },
                "graduation_project": {
                    "requirement": "مشروع التخرج (2 ساعة معتمدة)",
                    "duration": "يمكن تقسيمه على فصلين دراسيين"
                },
                "meeting_frequency": "يفضل مقابلة المرشد الأكاديمي قبل كل فترة تسجيل.",
                "advising_purpose": [
                    "تحديد المقررات المناسبة حسب التخصص",
                    "مراقبة الأداء الأكاديمي",
                    "مناقشة الخيارات المستقبلية (تدريب - مشروع - فرص عمل)"
                ]
            },
            "fees_structure": {
                "payment_policy": "الرسوم تحدد سنوياً بحد أقصى 5% زيادة للطلاب الجدد",
                "min_payment": "رسوم 12 ساعة معتمدة لكل فصل رئيسي"
            }
        }
        
        # Course descriptions
        self.course_descriptions = {
            "ECE-C101": {
                "title": "Digital Logic",
                "prerequisite": "GEN-C002",
                "topics": [
                    "Boolean algebra and logic gates (AND, OR, NAND, NOR)",
                    "Memory elements design",
                    "Sequential machines: synchronous & asynchronous",
                    "Digital circuit construction and troubleshooting"
                ]
            },
            "ECE-C102": {
                "title": "Computer Programming (1)",
                "prerequisite": "GEN-C002",
                "topics": [
                    "Problem solving, algorithms, flowcharting",
                    "Control structures, arrays, strings, matrices",
                    "Files, structured programming, software tools"
                ]
            },
            "ECE-C103": {
                "title": "Data Structure",
                "prerequisite": "ECE-C102",
                "topics": [
                    "Data types and memory allocation",
                    "File structures, sorting and searching",
                    "Algorithm analysis"
                ]
            },
            "ECE-C201": {
                "title": "Digital Electronics",
                "prerequisite": "ELE-C102",
                "topics": [
                    "Logic gates, Flip-flops, Memory, A/D & D/A Converters",
                    "Simplifying logic circuits, ALUs"
                ]
            },
            "ECE-C202": {
                "title": "Database (1)",
                "prerequisite": "ECE-C104",
                "topics": [
                    "Database models, data manipulation, SQL",
                    "Database design principles"
                ]
            },
            "ECE-C301": {
                "title": "Programmable Logic Controllers",
                "prerequisite": "ECE-C201",
                "topics": [
                    "PLCs architecture and programming, case studies"
                ]
            },
            "ECE-C302": {
                "title": "Operating Systems",
                "prerequisite": "ECE-C203",
                "topics": [
                    "OS types and functions, memory and process management"
                ]
            },
            "ECE-C401": {
                "title": "Digital Signal Processing",
                "prerequisite": "ECE-C303",
                "topics": [
                    "Digital filter design, spectral estimation, signal processors"
                ]
            },
            "ECE-C402": {
                "title": "Computer Network",
                "prerequisite": "ECE-C204",
                "topics": [
                    "Network design, protocols, routing, management"
                ]
            },
            "ECE-C405": {
                "title": "Artificial Intelligence",
                "prerequisite": "ECE-C307",
                "topics": [
                    "Prolog, search methods, image & language processing, expert systems"
                ]
            }
        }
        
        self.keywords = {
            "program": ["برنامج", "program", "تخصص", "specialization"],
            "credits": ["ساعات", "credits", "معتمدة", "credit hours"],
            "duration": ["مدة", "duration", "فترة", "period"],
            "requirements": ["متطلبات", "requirements", "شروط", "conditions"],
            
            "registration": ["تسجيل", "registration", "enrollment", "التحاق"],
            "gpa": ["معدل", "gpa", "grade point average", "المعدل التراكمي"],
            "semester": ["فصل", "semester", "term", "فصل دراسي"],
            
            "courses": ["مقررات", "courses", "subjects", "مواد"],
            "prerequisites": ["متطلبات سابقة", "prerequisites", "pre-requisites"],
            "course_code": ["كود المقرر", "course code", "رمز المقرر"],
            
            
            "grades": ["درجات", "grades", "marks", "علامات"],
            "grading": ["تقييم", "grading", "evaluation"],
            
            
            "attendance": ["حضور", "attendance", "presence"],
            "policies": ["سياسات", "policies", "rules", "قواعد"],
            "withdrawal": ["انسحاب", "withdrawal", "drop"],
            
            
            "advisor": ["مرشد", "advisor", "academic advisor", "مرشد أكاديمي"],
            "training": ["تدريب", "training", "internship"],
            "project": ["مشروع", "project", "graduation project", "مشروع التخرج"],
    
            
            "fees": ["رسوم", "fees", "tuition", "الرسوم الدراسية"],
            "payment": ["دفع", "payment", "pay"],
            
            
            "help": ["مساعدة", "help", "مساعدة", "support"],
            "menu": ["قائمة", "menu", "options", "خيارات"],
            "exit": ["خروج", "exit", "quit", "end", "إنهاء"]
        }
        
        self.current_language = "ar"  
        
    def detect_language(self, text):
        """Detect if text is Arabic or English"""
        arabic_chars = re.findall(r'[\u0600-\u06FF]', text)
        return "ar" if len(arabic_chars) > len(text) * 0.3 else "en"
    
    def get_response(self, user_input):
        """Main method to process user input and return response"""
        if not user_input.strip():
            return self.get_help_message()
        
        
        self.current_language = self.detect_language(user_input)
        user_input_lower = user_input.lower()
        
        
        if any(keyword in user_input_lower for keyword in ["exit", "quit", "end", "خروج", "إنهاء"]):
            return self.get_exit_message()
        
       
        if any(keyword in user_input_lower for keyword in ["help", "مساعدة", "menu", "قائمة"]):
            return self.get_help_message()
        
        
        response = self.process_program_info(user_input_lower)
        if response:
            return response
            
        response = self.process_registration_info(user_input_lower)
        if response:
            return response
            
        response = self.process_course_info(user_input_lower)
        if response:
            return response
            
        response = self.process_grading_info(user_input_lower)
        if response:
            return response
            
        response = self.process_policies_info(user_input_lower)
        if response:
            return response
            
        response = self.process_services_info(user_input_lower)
        if response:
            return response
            
        response = self.process_fees_info(user_input_lower)
        if response:
            return response
        
        
        return self.get_default_response()
    
    def process_program_info(self, user_input):
        """Process queries about program information"""
        if any(keyword in user_input for keyword in self.keywords["program"]):
            return self.get_program_info()
        
        if any(keyword in user_input for keyword in self.keywords["credits"]):
            return self.get_credits_info()
        
        if any(keyword in user_input for keyword in self.keywords["duration"]):
            return self.get_duration_info()
        
        if any(keyword in user_input for keyword in self.keywords["requirements"]):
            return self.get_admission_requirements()
        
        return None
    
    def process_registration_info(self, user_input):
        """Process queries about registration"""
        if any(keyword in user_input for keyword in self.keywords["registration"]):
            return self.get_registration_info()
        
        if any(keyword in user_input for keyword in self.keywords["gpa"]):
            return self.get_gpa_info()
        
        if any(keyword in user_input for keyword in self.keywords["semester"]):
            return self.get_semester_info()
        
        return None
    
    def process_course_info(self, user_input):
        """Process queries about courses"""
        if any(keyword in user_input for keyword in self.keywords["courses"]):
            return self.get_courses_overview()
        
        
        course_codes = re.findall(r'[A-Z]{3}-C\d{3}', user_input.upper())
        if course_codes:
            return self.get_course_details(course_codes[0])
        
        if any(keyword in user_input for keyword in self.keywords["prerequisites"]):
            return self.get_prerequisites_info()
        
        return None
    
    def process_grading_info(self, user_input):
        """Process queries about grading"""
        if any(keyword in user_input for keyword in self.keywords["grades"] + self.keywords["grading"]):
            return self.get_grading_info()
        
        return None
    
    def process_policies_info(self, user_input):
        """Process queries about policies"""
        if any(keyword in user_input for keyword in self.keywords["attendance"]):
            return self.get_attendance_policy()
        
        if any(keyword in user_input for keyword in self.keywords["policies"]):
            return self.get_policies_overview()
        
        if any(keyword in user_input for keyword in self.keywords["withdrawal"]):
            return self.get_withdrawal_policy()
        
        return None
    
    def process_services_info(self, user_input):
        """Process queries about student services"""
        if any(keyword in user_input for keyword in self.keywords["advisor"]):
            return self.get_advisor_info()
        
        if any(keyword in user_input for keyword in self.keywords["training"]):
            return self.get_training_info()
        
        if any(keyword in user_input for keyword in self.keywords["project"]):
            return self.get_project_info()
        
        return None
    
    def process_fees_info(self, user_input):
        """Process queries about fees"""
        if any(keyword in user_input for keyword in self.keywords["fees"] + self.keywords["payment"]):
            return self.get_fees_info()
        
        return None
    
    def get_program_info(self):
        """Get program information"""
        if self.current_language == "ar":
            return f"""
🎓 معلومات البرنامج:
• اسم البرنامج: {self.knowledge_base['program_name']}
• رمز البرنامج: {self.knowledge_base['program_code']}
• الجامعة: {self.knowledge_base['university']}
• الكلية: {self.knowledge_base['faculty']}
• الدرجة الممنوحة: {self.knowledge_base['degree_awarded']}
• نظام الدراسة: {self.knowledge_base['study_system']}
• لغة التدريس: {self.knowledge_base['language_of_instruction']}
"""
        else:
            return f"""
🎓 Program Information:
• Program Name: {self.knowledge_base['program_name']}
• Program Code: {self.knowledge_base['program_code']}
• University: {self.knowledge_base['university']}
• Faculty: {self.knowledge_base['faculty']}
• Degree Awarded: {self.knowledge_base['degree_awarded']}
• Study System: {self.knowledge_base['study_system']}
• Language of Instruction: {self.knowledge_base['language_of_instruction']}
"""
    
    def get_credits_info(self):
        """Get credits information"""
        if self.current_language == "ar":
            return f""" معلومات الساعات المعتمدة:
• إجمالي الساعات المطلوبة: {self.knowledge_base['total_required_credits']} ساعة معتمدة
• متطلبات الجامعة: {self.knowledge_base['requirements']['university']} ساعة معتمدة
• متطلبات الكلية: {self.knowledge_base['requirements']['faculty']} ساعة معتمدة
• متطلبات التخصص: {self.knowledge_base['requirements']['specialization']} ساعة معتمدة
"""
        else:
            return f"""
 Credit Hours Information:
• Total Required Credits: {self.knowledge_base['total_required_credits']} credit hours
• University Requirements: {self.knowledge_base['requirements']['university']} credit hours
• Faculty Requirements: {self.knowledge_base['requirements']['faculty']} credit hours
• Specialization Requirements: {self.knowledge_base['requirements']['specialization']} credit hours
"""
    
    def get_duration_info(self):
        """Get program duration information"""
        if self.current_language == "ar":
            return f"""
 مدة البرنامج:
• المدة القصوى: {self.knowledge_base['program_duration']}
• الحد الأدنى: {self.knowledge_base['registration']['min_duration']}
• الحد الأقصى: {self.knowledge_base['registration']['max_duration']}
"""
        else:
            return f"""
 Program Duration:
• Maximum Duration: {self.knowledge_base['program_duration']}
• Minimum Duration: {self.knowledge_base['registration']['min_duration']}
• Maximum Duration: {self.knowledge_base['registration']['max_duration']}
"""
    
    def get_admission_requirements(self):
        """Get admission requirements"""
        if self.current_language == "ar":
            requirements_text = "\n".join([f"• {req}" for req in self.knowledge_base['admission_requirements']])
            return f"""
 متطلبات القبول:
{requirements_text}
"""
        else:
            requirements_text = "\n".join([f"• {req}" for req in self.knowledge_base['admission_requirements']])
            return f"""
 Admission Requirements:
{requirements_text}
"""
    
    def get_registration_info(self):
        """Get registration information"""
        if self.current_language == "ar":
            return f"""
 معلومات التسجيل:
• الأهلية: {self.knowledge_base['registration']['eligibility']}
• الحد الأقصى للساعات في الفصل الدراسي:
  - معدل تراكمي أعلى من 3: {self.knowledge_base['registration']['max_credits_per_semester']['GPA_above_3']} ساعة
  - معدل تراكمي أعلى من 2: {self.knowledge_base['registration']['max_credits_per_semester']['GPA_above_2']} ساعة
  - معدل تراكمي أقل من 2: {self.knowledge_base['registration']['max_credits_per_semester']['GPA_below_2']} ساعة
• الحد الأقصى للفصل الصيفي: {self.knowledge_base['registration']['summer_max_credits']} ساعة معتمدة
"""
        else:
            return f"""
 Registration Information:
• Eligibility: {self.knowledge_base['registration']['eligibility']}
• Maximum Credits per Semester:
  - GPA above 3: {self.knowledge_base['registration']['max_credits_per_semester']['GPA_above_3']} credits
  - GPA above 2: {self.knowledge_base['registration']['max_credits_per_semester']['GPA_above_2']} credits
  - GPA below 2: {self.knowledge_base['registration']['max_credits_per_semester']['GPA_below_2']} credits
• Summer Maximum: {self.knowledge_base['registration']['summer_max_credits']} credits
"""
    
    def get_gpa_info(self):
        """Get GPA information"""
        if self.current_language == "ar":
            return f"""
 معلومات المعدل التراكمي:
• الحد الأدنى للتخرج: {self.knowledge_base['graduation_requirements']['minimum_gpa']}
• متطلبات التكريم: {self.knowledge_base['graduation_requirements']['honors_requirements']['minimum_gpa']}
• إنذار أكاديمي: {self.knowledge_base['policies']['academic_warning']}
"""
        else:
            return f"""
 GPA Information:
• Minimum for Graduation: {self.knowledge_base['graduation_requirements']['minimum_gpa']}
• Honors Requirements: {self.knowledge_base['graduation_requirements']['honors_requirements']['minimum_gpa']}
• Academic Warning: {self.knowledge_base['policies']['academic_warning']}
"""
    
    def get_semester_info(self):
        """Get semester information"""
        if self.current_language == "ar":
            return f"""
 معلومات الفصول الدراسية:
• الفصل الخريفي: {self.knowledge_base['semesters']['fall']}
• الفصل الربيعي: {self.knowledge_base['semesters']['spring']}
• الفصل الصيفي: {self.knowledge_base['semesters']['summer']}
"""
        else:
            return f"""
 Semester Information:
• Fall Semester: {self.knowledge_base['semesters']['fall']}
• Spring Semester: {self.knowledge_base['semesters']['spring']}
• Summer Semester: {self.knowledge_base['semesters']['summer']}
"""
    
    def get_courses_overview(self):
        """Get courses overview"""
        if self.current_language == "ar":
            uni_courses = "\n".join([f"• {course['code']}: {course['name']} ({course['credits']} ساعة)" 
                                   for course in self.knowledge_base['courses']['university_requirements']])
            elec_courses = "\n".join([f"• {course['code']}: {course['name']} ({course['credits']} ساعة)" 
                                    for course in self.knowledge_base['courses']['electrical_engineering_core']])
            return f"""
 نظرة عامة على المقررات:

متطلبات الجامعة:
{uni_courses}

المقررات الأساسية للهندسة الكهربية:
{elec_courses}

للمزيد من التفاصيل عن مقرر معين، اكتب كود المقرر (مثل: ECE-C101)
"""
        else:
            uni_courses = "\n".join([f"• {course['code']}: {course['name']} ({course['credits']} credits)" 
                                   for course in self.knowledge_base['courses']['university_requirements']])
            elec_courses = "\n".join([f"• {course['code']}: {course['name']} ({course['credits']} credits)" 
                                    for course in self.knowledge_base['courses']['electrical_engineering_core']])
            return f"""
 Courses Overview:

University Requirements:
{uni_courses}

Electrical Engineering Core Courses:
{elec_courses}

For more details about a specific course, type the course code (e.g., ECE-C101)
"""
    
    def get_course_details(self, course_code):
        """Get specific course details"""
        if course_code in self.course_descriptions:
            course = self.course_descriptions[course_code]
            if self.current_language == "ar":
                topics = "\n".join([f"• {topic}" for topic in course['topics']])
                return f"""
تفاصيل المقرر {course_code}:
• العنوان: {course['title']}
• المتطلبات السابقة: {course['prerequisite']}
• الموضوعات:
{topics}
"""
            else:
                topics = "\n".join([f"• {topic}" for topic in course['topics']])
                return f"""
 Course Details for {course_code}:
• Title: {course['title']}
• Prerequisite: {course['prerequisite']}
• Topics:
{topics}
"""
        else:
            if self.current_language == "ar":
                return f" عذراً، لا توجد معلومات متاحة للمقرر {course_code}"
            else:
                return f" Sorry, no information available for course {course_code}"
    
    def get_prerequisites_info(self):
        """Get prerequisites information"""
        if self.current_language == "ar":
            return """
 معلومات المتطلبات السابقة:
• يجب إكمال المتطلبات السابقة قبل التسجيل في المقرر
• يمكن التحقق من المتطلبات السابقة لكل مقرر
• اكتب كود المقرر لمعرفة متطلباته السابقة
"""
        else:
            return """
 Prerequisites Information:
• Prerequisites must be completed before registering for a course
• Prerequisites can be checked for each course
• Type the course code to see its prerequisites
"""
    
    def get_grading_info(self):
        """Get grading information"""
        if self.current_language == "ar":
            grades_text = "\n".join([f"• {grade}: {gpa}" for grade, gpa in self.knowledge_base['grading_scale'].items()])
            return f"""
 نظام التقييم:
{grades_text}
"""
        else:
            grades_text = "\n".join([f"• {grade}: {gpa}" for grade, gpa in self.knowledge_base['grading_scale'].items()])
            return f"""
 Grading Scale:
{grades_text}
"""
    
    def get_attendance_policy(self):
        """Get attendance policy"""
        if self.current_language == "ar":
            return f"""
 سياسة الحضور:
{self.knowledge_base['policies']['attendance']}
"""
        else:
            return f"""
 Attendance Policy:
{self.knowledge_base['policies']['attendance']}
"""
    
    def get_policies_overview(self):
        """Get policies overview"""
        if self.current_language == "ar":
            return f"""
 السياسات الأكاديمية:
• الحضور: {self.knowledge_base['policies']['attendance']}
• الإنذار الأكاديمي: {self.knowledge_base['policies']['academic_warning']}
• إعادة المقرر: {self.knowledge_base['policies']['course_repeat']}
• الانسحاب: {self.knowledge_base['policies']['withdrawal']}
"""
        else:
            return f"""
 Academic Policies:
• Attendance: {self.knowledge_base['policies']['attendance']}
• Academic Warning: {self.knowledge_base['policies']['academic_warning']}
• Course Repeat: {self.knowledge_base['policies']['course_repeat']}
• Withdrawal: {self.knowledge_base['policies']['withdrawal']}
"""
    
    def get_withdrawal_policy(self):
        """Get withdrawal policy"""
        if self.current_language == "ar":
            return f"""
 سياسة الانسحاب:
{self.knowledge_base['policies']['withdrawal']}
"""
        else:
            return f"""
 Withdrawal Policy:
{self.knowledge_base['policies']['withdrawal']}
"""
    
    def get_advisor_info(self):
        """Get academic advisor information"""
        if self.current_language == "ar":
            purposes = "\n".join([f"• {purpose}" for purpose in self.knowledge_base['student_services']['advising_purpose']])
            return f"""
 معلومات المرشد الأكاديمي:
• {self.knowledge_base['student_services']['academic_advisor']}
• {self.knowledge_base['student_services']['meeting_frequency']}
• أغراض الإرشاد:
{purposes}
"""
        else:
            purposes = "\n".join([f"• {purpose}" for purpose in self.knowledge_base['student_services']['advising_purpose']])
            return f"""
 Academic Advisor Information:
• {self.knowledge_base['student_services']['academic_advisor']}
• {self.knowledge_base['student_services']['meeting_frequency']}
• Advising Purposes:
{purposes}
"""
    
    def get_training_info(self):
        """Get training information"""
        if self.current_language == "ar":
            return f"""
 معلومات التدريب الميداني:
• المتطلب: {self.knowledge_base['student_services']['industrial_training']['requirement']}
• الساعات المعتمدة: {self.knowledge_base['student_services']['industrial_training']['credits']} ساعة معتمدة
"""
        else:
            return f"""
 Industrial Training Information:
• Requirement: {self.knowledge_base['student_services']['industrial_training']['requirement']}
• Credits: {self.knowledge_base['student_services']['industrial_training']['credits']} credit hours
"""
    
    def get_project_info(self):
        """Get graduation project information"""
        if self.current_language == "ar":
            return f"""
 معلومات مشروع التخرج:
• المتطلب: {self.knowledge_base['student_services']['graduation_project']['requirement']}
• المدة: {self.knowledge_base['student_services']['graduation_project']['duration']}
"""
        else:
            return f"""
 Graduation Project Information:
• Requirement: {self.knowledge_base['student_services']['graduation_project']['requirement']}
• Duration: {self.knowledge_base['student_services']['graduation_project']['duration']}
"""
    
    def get_fees_info(self):
        """Get fees information"""
        if self.current_language == "ar":
            return f"""
 معلومات الرسوم:
• سياسة الدفع: {self.knowledge_base['fees_structure']['payment_policy']}
• الحد الأدنى للدفع: {self.knowledge_base['fees_structure']['min_payment']}
"""
        else:
            return f"""
 Fees Information:
• Payment Policy: {self.knowledge_base['fees_structure']['payment_policy']}
• Minimum Payment: {self.knowledge_base['fees_structure']['min_payment']}
"""
    
    def get_help_message(self):
        """Get help message with available keywords"""
        if self.current_language == "ar":
            return """
 مرحباً بك في المساعد الآلي لبرنامج الهندسة الكهربية والحاسبات!

 الكلمات المفتاحية المتاحة:
• برنامج / program - معلومات البرنامج
• ساعات / credits - الساعات المعتمدة
• مدة / duration - مدة البرنامج
• متطلبات / requirements - متطلبات القبول
• تسجيل / registration - معلومات التسجيل
• معدل / gpa - معلومات المعدل التراكمي
• فصل / semester - معلومات الفصول الدراسية
• مقررات / courses - نظرة عامة على المقررات
• متطلبات سابقة / prerequisites - المتطلبات السابقة
• درجات / grades - نظام التقييم
• حضور / attendance - سياسة الحضور
• سياسات / policies - السياسات الأكاديمية
• انسحاب / withdrawal - سياسة الانسحاب
• مرشد / advisor - معلومات المرشد الأكاديمي
• تدريب / training - التدريب الميداني
• مشروع / project - مشروع التخرج
• رسوم / fees - معلومات الرسوم
• مساعدة / help - هذه القائمة
• خروج / exit - إنهاء المحادثة

 يمكنك أيضاً كتابة كود مقرر معين (مثل: ECE-C101) للحصول على تفاصيله
"""
        else:
            return """
 Welcome to the Electrical and Computer Engineering Program Assistant!

 Available Keywords:
• program - Program information
• credits - Credit hours information
• duration - Program duration
• requirements - Admission requirements
• registration - Registration information
• gpa - GPA information
• semester - Semester information
• courses - Courses overview
• prerequisites - Prerequisites information
• grades - Grading system
• attendance - Attendance policy
• policies - Academic policies
• withdrawal - Withdrawal policy
• advisor - Academic advisor information
• training - Industrial training
• project - Graduation project
• fees - Fees information
• help - This menu
• exit - End conversation

💡 You can also type a specific course code (e.g., ECE-C101) for course details
"""
    
    def get_default_response(self):
        """Get default response when no specific match is found"""
        if self.current_language == "ar":
            return """
 لم أفهم سؤالك. يمكنك استخدام الكلمات المفتاحية التالية:
• برنامج، ساعات، مدة، متطلبات، تسجيل، معدل، فصل، مقررات، درجات، حضور، سياسات، مرشد، تدريب، مشروع، رسوم

أو اكتب "مساعدة" للحصول على قائمة كاملة بالكلمات المفتاحية.
"""
        else:
            return """
 I didn't understand your question. You can use these keywords:
• program, credits, duration, requirements, registration, gpa, semester, courses, grades, attendance, policies, advisor, training, project, fees

Or type "help" for a complete list of keywords.
"""
    
    def get_exit_message(self):
        """Get exit message"""
        if self.current_language == "ar":
            return """
 شكراً لك لاستخدام المساعد الآلي لبرنامج الهندسة الكهربية والحاسبات!
نتمنى لك التوفيق في دراستك! 🎓
"""
        else:
            return """
 Thank you for using the Electrical and Computer Engineering Program Assistant!
Good luck with your studies! 🎓
"""

def main():
    """Main function to run the chatbot"""
    chatbot = StudentChatbot()
    
    print("=" * 60)
    print(" مساعد برنامج الهندسة الكهربية والحاسبات")
    print(" Electrical and Computer Engineering Program Assistant")
    print("=" * 60)
    print(chatbot.get_help_message())
    print("=" * 60)
    
    while True:
        try:
            user_input = input("\n أنت / You: ").strip()
            
            if not user_input:
                continue
                
            response = chatbot.get_response(user_input)
            print(f"\n المساعد / Assistant: {response}")
            
            # Check if user wants to exit
            if any(keyword in user_input.lower() for keyword in ["exit", "quit", "end", "خروج", "إنهاء"]):
                break
                
        except KeyboardInterrupt:
            print("\n\n" + chatbot.get_exit_message())
            break
        except Exception as e:
            print(f"\n حدث خطأ / An error occurred: {e}")
            print("يرجى المحاولة مرة أخرى / Please try again.")

if __name__ == "__main__":
    main() 