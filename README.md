# مِدار — Midar

منصة عربية متعددة المستخدمين مبنية بـNext.js وPostgreSQL وDrizzle. تتضمن تسجيلاً بالبريد وكلمة المرور، تفعيلاً بكود من أربعة أرقام، جلسات آمنة، حسابات منفصلة، دفتر أوامر داخلي، طلبات محافظ، ولوحة مطور كاملة.

## التشغيل على GitHub Codespaces

هذه هي طريقة تشغيل المشروع كاملاً على GitHub؛ أما **GitHub Pages** فلا يناسب هذا المشروع لأنه يستضيف ملفات ثابتة فقط ولا يشغّل Next.js Route Handlers أو PostgreSQL.

1. ارفع المشروع إلى مستودع GitHub.
2. من صفحة المستودع اختر **Code → Codespaces → Create codespace on main**.
3. يقوم Dev Container تلقائياً بتشغيل PostgreSQL، وتثبيت الحزم، وإنشاء ملف `.env` خاص، وتطبيق الجداول.
4. بعد اكتمال التهيئة تفتح المنصة من المنفذ **3000** في تبويب **Ports**.
5. قاعدة البيانات محفوظة في Docker Volume باسم `midar_postgres_data`.

إذا لم يبدأ الخادم تلقائياً بعد إعادة فتح Codespace:

```bash
npm run dev
```

## الدخول أثناء التطوير

- المستخدمون: `/register` ثم `/activate`، والدخول لاحقاً من `/login`.
- لوحة المطور: `/developer/login`.
- البريد الابتدائي: `developer@midar.app`.
- كلمة المرور الابتدائية للتطوير: `900600`.

غيّر كلمة مرور المطور و`AUTH_SECRET` قبل أي نشر عام. لا ترفع `.env`؛ الملف مستبعد من Git. يمكن حفظ القيم الإنتاجية في **Codespaces Secrets** أو أسرار بيئة الاستضافة.

## GitHub Actions

كل Push أو Pull Request يشغّل `.github/workflows/ci.yml` وينفّذ:

- PostgreSQL 16 كخدمة مستقلة.
- تثبيت الاعتمادات وتطبيق مخطط Drizzle.
- `next typegen` وفحص TypeScript.
- بناء Next.js الإنتاجي.

## التشغيل المحلي بالأوامر

يتطلب Docker لقاعدة البيانات، وNode.js 22 للتطبيق:

```bash
cp .env.example .env
# استبدل AUTH_SECRET بقيمة عشوائية طويلة قبل التشغيل الدائم.
docker compose up -d db
npm install
npx drizzle-kit push
npm run dev
```

ثم افتح `http://localhost:3000`.

## متغيرات البيئة

- `DATABASE_URL`: اتصال PostgreSQL.
- `AUTH_SECRET`: سر عشوائي طويل لحماية أكواد التفعيل.
- `DEVELOPER_EMAIL` و`DEVELOPER_INITIAL_PASSWORD`: إنشاء حساب المطور عند أول دخول فقط.
- `SUPABASE_URL` و`SUPABASE_PUBLISHABLE_KEY`: اختياريان. مفتاح Supabase Publishable وحده لا يحتوي عنوان المشروع ولا يكفي للاتصال.

## حدود التنفيذ

الحسابات والمستخدمون والجلسات والأكواد والأرصدة والطلبات محفوظة فعلياً في PostgreSQL. تنفيذ الأوراق المالية داخلي في دفتر مِدار بأسعار استرشادية، ولا يُرسل إلى بورصة أو وسيط خارجي. اعتماد تحويل المحفظة يتم يدوياً من المطور بعد التحقق من العملية.
