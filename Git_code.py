#  اليوم انتهيت من فهم الجت بعدما كان صندوق اسود 
# الجت مهم جدا بالنسبه لكل مبرمج لحفظ التعديلات و الرجوع للتعديلات القديمة و العمل الجماعي
# اذا كنت تشبهني اختصر الحياة و اطلع على ملخصي

""" المستوى 1: أساسيات Git (لازم قبل GitHub)
تثبيت Git على جهازك
فهم كلمات Git الأساسية:
repository
commit
stage / staging area
branch
إنشاء مشروع Git جديد
إضافة ملفات
عمل أول commit
فهم حالة الملفات:
untracked
staged
modified
"""

""" المستوى 2: العمل الاحترافي بـ Git
استخدام الفروع (branches)
الدمج (merge)
حلّ تعارضات الدمج (merge conflicts)
إعادة كتابة التاريخ (reset / revert)
تجاهل ملفات (gitignore)
"""

""" المستوى 3: أساسيات GitHub
إنشاء حساب GitHub
رفع مشروع من جهازك إلى GitHub
استنساخ مشروع clone
push / pull
إنشاء مستودع جديد
إدارة المفاتيح (SSH Key)
"""

""" المستوى 4: احتراف GitHub
الـ Pull Request
الـ Issues
GitHub Projects
GitHub Actions
التعاون بين فرق العمل
حماية الفروع Branch Protection
الـ Fork
"""


""" كلمات Git الأساسية:
repository           ذاكرة المشروع
Working Directory    المجلد العادي اللي فيه ملفاتك
Staging Area         المكان الي تنظاف فيه الملفات الي نرد نحفظها git add لما نعمل
commit               الحفظ الرسمي
staging area branch  وتقدر تسوي فرع جديد باسم للتعديل بدون لمس النسخة الأصلية
untracked            شايفها… لكنها مو مضافة Git ملفات في المجلد
modified             commit للملف و باقي تعمل git add يعني عملت 
committed            يعني: تم حفظ الملف رسميًا
"""
# ==============================================================================



# ==============================================================================

# -------------------------------- Git اعدادات ---------------------------------

# vs code يشتغل في Git التأكد إن
# git --version

# انشاء مستودع
# git init

# اظهار الملفات الموجودة الغير مضافة
# git status

# من أنت لتسجل اسمك وبريدك في تاريخ المشروع Git لنعرف
# git config --global user.name "Hamid"
# git config --global user.email "alalbah@gmail.com"

# أضافة التعديلات و الملفات
# git add hello.txt login.py
# أو
# git add .

# اذا تريد تنتقل فرع ثاني بس ما تريد ترفع الملفات بعدك احفض التعديلات مؤقتا
# git stash
# بعد ما ترجع اعمل
# git stash pop

# الحفظ الرسمي Commit عمل 
# رسالة تشرح نوع التغيير message اختصار لكلمة  = -m
# git commit -m "My first commit"

# اللي سويتها أثناء العمل commits كيف تشوف قائمة كل الـ
# git log            كل التفاصيل
# git log --oneline  مختصر 

#  لتشوف أسماء الملفات اللي تغيّرت 
# اسم الملفات و كم سطر تغيّر
# git log --stat

# شوف الفروع الموجودة فيه
# git branch

# إنشاء فرع جديد
# git branch feature-login

# للتنقل بين الفروع
# تلاحض كل فرع عنده نفس الملفات لاكن اكوادها مختلفة حسب التعديل
# git switch main    

# نفّذ الدمج
# لازم تقف على الفرع الي تريده يتعدل
# ملاحظة اذا دمجت و فرع ثاني اراد يدمج و هو معدل نفس الاسطر الي انت عدلتهن راح يظهر تنبيه و يحتاج تختاروا بشكل يدوي
# git merge feature-login

# كيف أرجع لنسخة قديمة
# git log --oneline
# commit رقم الـ
# git checkout ba87665
# او
# git switch --detach ba87665

# القديم commitطرق الرجوع للـ
# -- git reset --
# و التعديلات و يقف على المختار commit يحذف الـ
# git reset --hard B
# commit يبقى تعمل git add و يحتفظ بالتعديلات كنك عامل commitيحذف الـ
# git reset --soft HEAD~1
# ولا يحذف التعديلات من الملف git add و الـ commit يحذف الـ
# git reset --mixed HEAD~1 أو git reset HEAD~1
# -- git revert --
# المختار commit جديدًا من الـ commit بل ينشئ commit لا يحذف الـ 
# git revert C

# يمكن استرجاعه باستخدام reset باستخدام commit إذا حذفت
# git reflog
# ID ثم بالـ
# git reset --hard f6a7594  
# التعديلات ما ترجع اذا عملت 
# git reset f6a7594  


# commit إذا أردت تتصفح النسخة القديمة في
# git checkout ba87665
# Git الحديث
# git switch --detach ba87665

# commit عرض التغييرات قبل عمل 
# git diff

# لحذف ملف من الفرع
# git rm test.py
# git commit -m "Remove test.py"

# لحذف فرع
# التي تم دمجها في فرع آخر commits طبعا حذف الفرع لا يعني حذف الـ
# git branch -d branch-name
# branch is not fully merged لم يتم دمجها commits اذا ظهرت رسالة يعني يوجد 
# إذا كنت متأكدًا أنك تريد حذف بكل الاحوال
# git branch -D branch-name

# -------------------------------- GitHup مع Git اعدادات ربط ---------------------------------

# vs code اكتب في
# يعرض المجلد الحالي الذي تعمل بداخله
# pwd

# GitHup ربط المشروع الحالي بمستودع
# مثل GitHupالرابط الي اعطاك اياه الـ
# git remote add origin https://github.com/s1j2b1/Git_learn.git
# GitHup ربط الملف الحالي بمستودع مختلف في
# https://github.com/s1j2b1/Git_learn.git

# للتأكد باي مستودع مربوط
# git remote -v

# رفع المشروع لأول مرة
# git push -u origin main
# المرات القادمة يكفي
# git push





# -------------------------------------------------------------------


# الإعداد الأولي (مرة واحدة فقط)
# من أنت GitHub قبل أن ترفع، يجب أن يعرف
# git config --global user.name "sulaiman"
# git config --global user.email "s1j2b1@gmail.com"

# أنشئ نيو هستري على الجت هب بيعطيك هذلا الكودات لربط الجت هب مع التيرمنل

# اذا كان الهستري ما يزال فارغ
# …or create a new repository on the command line

# اذا رفعت ملفات على هذا الهستري قبل
# …or push an existing repository from the command line


# -----------------------------
# هذه هي "الخطة" التي ستكررها كلما أجريت تعديلاً:

# قبل أن ترفع أي شيء ليظهر قائمة بالملفات التي عدلتها ولم ترفعها بعد
# git status.

# التجهيز (Stage):
# git add .

# التثبيت (Commit): سجل التعديلات مع وصف (رسالة)
# git commit -m "تحديث واجهة لوحة التحكم وتحسين خوارزمية التنبؤ"

# الرفع اول مرة (Push):
# git push -u origin main
# المرات القادمة فقط تحديث
# git push


# --------------------------- ملاحظات ---------------------------
# لرفع ملف محدد:
# git add file1 name.py file2 name.py


# لرفع كل الملفات (عدا المستثناة): النقطة تعني كل شيء في هذا المجلد
# git add .


# كيف تستثني ملفات لا تريد رفعها؟ (ملفات خاصة!)
# .gitignore أنشئ ملفاً في مجلد المشروع اسمه 







