import os

import telebot
import random
from random import choice

TOKEN = '5313426482:AAF7S1tmRnqKmxZQbISdrkJqYawlpqj03jc'  # Токен моего бота

bot = telebot.TeleBot(TOKEN)  # Подключение токена

emoje = [
    '😍', "🥰", "😘", "😻", "💋", "😚", "❤️", "🧡", "💛", "💚", "💙", "💜", "❤️‍🔥", "❣️", "💕", "💞", "💓", "💗", "💖",
    "💘", "💝", "💟", "♥️"
]  # эмоджи

ilove = ["Навахо	Ayóó ánííníshí	Аийоо ианинииши",
         "Эсперанто	Mi amas vin	ми амас вин",
         "Алеутский	Txin yaxtakuq	Тхкин яхктакуг",
         "Гавайский	Aloha wau iā ʻoe	Алоха ва уйа ой",
         "Португальский	Аmo-te, eu te amo	аму ти, эу ти аму",
         "Инуктикут	ᓇᒡᓕᒋᕙᒋᑦ	НааглИигивадгит",
         "Датскй	Jeg elsker dig	йяй элске(р) дай",
         "Итальянский	ti amo	ти амо",
         "Украинский	Я тебе кохаю	я тэбэ кохаю",
         "Финский	Minä rakastan sinua	миня ракастан синуа",
         "Французский	Je t'aime	жэ тэм",
         "Чешский	Milujite	милую цэ",
         "Валлийский	Dw i’n dy garu di	Дуо ин дгару де(и)",
         "Шведский	Jag älskar dig	я эльскар дэй",
         "Луле саамский	Mån æhtsáv duv	Мияй эхтсау дау",
         "Эстонский	Ma armastan sind	ма армастан синт",
         "Hемецкий	ich liebe dich	ихь либэ дихь",
         "Польский	Kocham cie	кохам че",
         "Азербайджанский	mən səni sevirəm	мэн сэни севирэм",
         "Армянский	Tս քեզ սիրում եմ։ (es qez sirum em)	ес кэс сирум эм",
         "Боснийский и хорватский	Volim te	Волим те",
         "Болгарский	Aз те обичам	аз те обичам",
         "Латышский	es tevi milu	эс тэви милу",
         "Bенгерский	Szeretlek	сэрэтлэк",
         "Ирландский	tá grá agam ort	та гра агэморт",
         "Греческий	σ΄αγαπώ/ σας αγαπώ	сагапо (неформально)",
         "сас агхапо (формально)",
         "Грузинский	მე შენ მიყვარხარ	мэ шен миквархар",
         "Hидерландский	ik hou van jou	ик хау ван яу",
         "Абхазский	Сара бара бзия бзой!	Сара бара бзия бзой",
         "Адыгейский	Сэ оры плэгун!	Сэ оры плэгун!",
         "Белорусский	Я цябе кахаю	Я цябе кахаю",
         "Исландский	Ég elska þig	Е эльска гых",
         "Испанский	Te amo	Тэ амо",
         "Каталонский	T'estimo	Тэстимо",
         "Словацкий	Íúbim ta	Любим тя",
         "Словенский	Ljubim te	Любим те",
         "Басков язык (баскский)	Maite zaitut	Маитэ заитут",
         "Гагаузский	Бянь сени бинерим	Бянь сени бинерим",
         "Драконьи руны	Язык Драконьи рунны	Иии хааашш ууу",
         "Древнегреческий язык	Ἀγαπῶ σε	Эго агапо су",
         "Корсиканский	Ti tengu caru	Ти тенгю кару",
         "Курдский	Ez ji te hez dikim	Эз жи те хэз дыкым",
         "Крымско-татарский	Men seni sevem	Мэн сэни сэвэм",
         "Латинский	Te amo	Тэ амо",
         "Македонский	Tе сакам, tе љубам	Тэ сакам, тэ любам",
         "Мальтийский	Inhobbok	Ингоббок",
         "Норвежский	Egelskardeg	Яй эльскарь дай",
         "Сербский	Волим те	Волим те",
         "Фламандский	Ik zie oe geerne	Икзие ое геерне",
         "Казахский	мен сені жақсы көремін	мен сени жаксы коремин",
         "Монгольский	Би чамд хайртай	Би чамд хайртай",
         "Иврит	אני אוהב אותך",
         "אני אוהבת אותך	анИ оЭв отАх мужчина женщине",
         "анИ оЭвэт отхА женщина мужчине",
         "Урду	میں آپ سے محبت کَرتا ہوں	Ммеинап сау мхабат карта хун",
         "Bьетнамский	Tôi yêu bạn	Той иу бан",
         "Корейский	사랑해	саранхэ",
         "Китайский (мандаринское наречие)	我愛你[我爱你]	во ай ни",
         "Непальский	म तपाईं प्रेम	Ма тимиилал майа гарс(ц)шу",
         "Тибетский	ང་ཁྱེད་རང་ལ་དགའ་པོ་ཡོད་	nga kayrâng-la gawpo yö Нга кайариан(г)- гупо ийоо",
         "Японский	愛してるよ",
         "愛してるわ	айшитеру йо(мужское) айшитеру уа(женское)",
         "Арамейский	ܟܠܐܢܐܡܝܪ	Кадиух би айван",
         "Ассирийский		Ана ух маххубэ",
         "Бангладешский	আমিতোমাকেভালবাসি	Ами тумакэ палабаши",
         "Киргизский	Мен сени сүйөм	Мен сэни сюйом",
         "Лао	ຂ້ອຍຮັກເຈົ້າ	кхойхактяо",
         "Ливанский	Bahibak	Бахибак",
         "Малайский	Saya sayangkan kamu	Сая саянкан каму",
         "Таджикский	Ман туро дӯст медорам	Ман туро дёст медорам",
         "Тайваньский	Wa ga ei li	Ва га эй ли",
         "Тайский	ผมรักคุณ	Пхом рак кхун",
         "Узбекский	Мен сени севаман	Мэн сэни севаман",
         "Туркменский	Men seni söýýärin	Мен сени сёйярин",
         "Маратхи	मीतुझ्यावरप्रेमकरतो	Ми тужавар прэм карту",
         "Сингальский (язык сигналов)	язык сигналов	ам а о йа та аа да ре йи",
         "Суахили	Ninakupenda	нинакупенда",
         "Камбоджийский	Bon soro lanh oon	Буон соро лах оон",
         "Сомали	Waan ku jecelahay	Ваан ку ийесцелахаи",
         "Африкаанс	Ek’s lief vir jou	эк эс лиф фир йу",
         "Йорубу (а)	Mo nifẹẹ rẹ	Мо нифии риэ",
         "Амхарский	አፈቅርሻለሁ።",
         "አፈቅርሀለሁ።	афекири шалеху(женский вариант) афекири шалех(мужской вариант)",
         "Йоруба	Mo nifẹẹ rẹ (mo ni ife re)	Мо нифе рэ",
         "Aлбанский	Unë të dua	ен тэ дуа",
         "Турецкий	Seni seviyorum	сени севиёрум",
         "Персидский		дуст-ат дарам",
         "Aрабский(Египетский)	ٲنَا بحِبَّك	Ана ахебек",
         "Пушту	Язык Пушту	За ста сара мина кавом ",
         ]  # я тебя люблю на 100 разных языках

brt = ["Мамочка, самый светлый и родной человек в моей жизни. Как бы женщины не печалились, что с годами их молодость уходит, \
    для меня твой День Рождения – всегда будет лучшим и главным праздником! Весь это тот самый день, когда на свет появился человек, \
    без которого мое существование было бы невозможно. Я желаю тебе крепкого здоровья, потому что все остальное у тебя есть – твои дети, твое счастье, \
    красота, которая живет в каждом, богатство – твоя семья и близкие. Мы всегда будем рядом, радовать тебя, поддерживать во всем и любить. Сияй в свой \
    праздник, мы все тебя искренне поздравляем!\
    Пусть сегодня у тебя будет только хорошее настроение, ароматные цветы и теплые слова!",
       "Дорогая мамочка! Поздравляю тебя с днем рождения! Желаю тебе здоровья, счастья и радости, пусть в твоем сердце всегда \
       живет любовь! Я очень люблю тебя, и хочу, чтобы ты была всегда в прекрасном настроении, чтобы в твоих красивых глазах чаще светилась радость, \
       а на губах играла улыбка! Пусть у тебя на душе будет светло и спокойно, а в жизни будет больше приятных событий, интересных встреч и счастливых моментов. \
       И еще – я благодарю судьбу за то, что у меня такая хорошая мама. Спасибо тебе за все, и дай Бог тебе здоровья и долгой счастливой жизни!\
       А я постараюсь сделать все для того, чтобы радости и тепла в ней было больше.",
       'С днём рождения, мама! Ты – главное, что у меня есть. Я люблю тебя и желаю для тебя только самого лучшего: \
       здоровья и красоты, удачи и успехов, любви и счастья. Пусть небо над тобой всегда будет чистым, дорога твоя легка, \
       дом – полная чаша, а люди рядом – лучшими из лучших. Поздравляю!',
       'Любимая мамочка, с днем рождения! Спасибо тебе за жизнь, за все, что ты для нас сделала. Живи долго-долго, не болей, \
       не старей, никогда не печалься, а только улыбайся и радуйся жизни. \
       Пускай каждый день тебя радует, здоровье не подводит, близкие и родные не огорчают. Мечты твои все пускай сбываются, счастье наполняет дом.',
       'Дорогая мамуля, с днем рождения тебя! Самого крепкого тебе здоровья, долгих и счастливых лет жизни. Хочу, чтобы ты всегда оставалась молодой, красивой и, конечно, любимой всеми родными и близкими. Пускай в твоей жизни не будет печалей, не решенных проблем, неприятных событий. Только радость и удача пускай сопутствуют во всем',
       'Мамочка, родная, поздравляю тебя с Днем рождения! Ты – самая замечательная на свете! Мой близкий друг и мудрый советчик! Я очень тобой горжусь и восхищаюсь! Я хочу, чтобы улыбка почаще озаряла твое прекрасное лицо! Получай удовольствие от каждой минуты своей жизни и будь счастлива!',
       'Мамочка, дорогая, от всего сердца поздравляю тебя с Днем рождения! В этот прекрасный день так много всего хочется тебе пожелать! Мамочка, я желаю тебе такого крепкого здоровья, чтобы ты о нем не вспоминала, а всегда ощущала себя восемнадцатилетней! Желаю просыпаться каждый день с радостным ощущением счастья и восторга в сердце! Пусть каждый новый день делает тебя еще мудрее, но не старше! Желаю тебе сохранить ту доброту, тепло и гармонию с самой собой и миром, которая живет в тебе! Пусть почаще твои прекрасные, самые любимые на свете, глаза светятся от счастья! Самых долгих и самых прекрасных лет тебе, мамочка!',
       'Дорогая моя мамулечка! Я поздравляю тебя с днём рождения и желаю, чтобы ты никогда не грустила! Мне очень нужна твоя ласковая улыбка и счастливый блеск твоих глаз. Мама, знай, что именно благодаря тебе я выросла такой, какая я есть, и мне очень хочется, чтобы ты мной гордилась и радовалась за меня. Ты привила мне главные жизненные ценности, ты всегда была и остаёшься для меня идеалом женщины и примером во всём!',
       'Поздравляю тебя с днём рождения, моя любимая мамочка, мой самый родной и близкий человечек! Желаю, чтобы твоё сердце переполняла радость, чтобы все дела спорились, чтобы побольше времени ты проводила просто в своё удовольствие. Спасибо, что ты у меня есть! Спасибо за твою заботу, ласку, за нежность твоих рук и за правильные ориентиры, привитые мне с детских лет. Свет в твоих окнах и в твоих глазах – это самая важная ценность для меня, пусть он горит вечно!',
       'Наша драгоценная и незаменимая мамочка! Поздравляем тебя с днем рождения и желаем только лучшего. Пусть крепкое здоровье поддерживает твою красоту и цветение, пусть удача приносит тебе в дар всё, о чём ты мечтаешь, пусть рядом с тобой всегда будут любовь и счастье, и глаза твои сияют радостью. Хотим, чтобы ты всегда оставалась молодой, прекрасной и весёлой!',
       'Моя родная, дорогая мамочка, сегодня день твоего рождения, и весь мир вокруг как будто преобразился. Смотри, даже солнышко дарит тебе свои лучи, воздух особенно чист, а пение птиц – звонче. Моя родная, я желаю, чтобы твоё настроение всегда было таким же безоблачным, как это небо над головой! Чтобы радость переполняло твоё большое, доброе сердце! Крепкого тебе здоровья, живи счастливо много-много лет!',
       'Мама! Поздравляю тебя с днём рождения! Пусть бьёт фонтаном позитив, пусть в глазах твоих всегда горит искорка задора, пусть исполняются все твои желания! Ты у меня – самая красивая, молодая, заводная, яркая! Я с детства горжусь тобой, и очень хочу, чтобы ты тоже гордилась мной. Я посвящаю тебе все успехи в своей жизни. Прости, что иногда расстраиваю и невольно заставляю переживать. Я люблю тебя, мамуля, всем сердцем! Ты – мой самый близкий друг и мой земной ангел-хранитель!',
       'Моя любимая мамочка. Сегодня, в твой день рождения хочу выразить тебе всю свою любовь и признательность. Ты всегда была рядом: радовалась моим успехам, помогала решать проблемы, поддерживала в трудных ситуациях. Благодаря тебе мне удалось преодолеть многие жизненные преграды. Желаю тебе всегда оставаться такой же жизнерадостной, уверенной в себе оптимисткой. Крепкого тебе здоровья, долгих лет жизни!',
       'С Днём рождения, мама! Пусть каждый прожитый год добавляет тебе красоты! Ты самый добрый, самый мудрый, самый лучший человек на свете и заслуживаешь счастья, как никто другой! Пусть оно никогда не покидает тебя, пусть улыбка почаще озаряет твоё прекрасное лицо! Я желаю тебе много солнечных дней, высокого, безоблачного неба над головой, радости, удачи и тепла!',
       'Мама, от всего сердца поздравляю тебя с днем рождения. Желаю тебе самого драгоценного – здоровья! Пускай стороной обходят тебя все проблемы, невзгоды и несчастья, печаль никогда не появляется в твоих глазах. В этот день хочу подарить тебе всю свою любовь, тепло, внимание и заботу. Живи долго, радуй всех своей лучезарной улыбкой, дари радость общения.',
       'День рождения моей дорогой мамы отмечаем мы всей семьей! Мое сердце переполнено любовью к тебе, мне так много хочется тебе пожелать. И очень хочется, чтобы все мои пожелания непременно сбылись. Я желаю тебе отменного здоровья и сделаю все, что от меня зависит, чтобы твое здоровье было действительно хорошим. Всего этого ты заслужила. Ты заботилась о нас, своих детях, мы купались в твоей любви и твоем добром отношении к нам. Теперь очередь наша окружить тебя любовью и заботой. Мы всем сердцем любим свою маму!'
       'Мамочка, родная! Огромного богатства я желаю тебе в этот праздничный день. Богатства в твоей семье, где дружно живут дети внуки, любимый супруг. Богатства в здоровье. Богатства в друзьях. Богатства в каждом наступающем дне. Нам так хорошо с милой нашей мамой!',
       'Мамочка! Ты для меня, как подруга, как старшая сестра. Я могу поделиться с тобой своим счастьем, я могу поведать тебе свои горести и печали. Ты - Ангел Хранитель, который ведет меня по жизни и не дает оступиться. Ты подарила мне самое ценное - жизнь. Я постараюсь прожить ее так, чтобы ты гордилась мной, чтобы никогда тебе не было за меня стыдно. Я постараюсь быть для своих детей такой же хорошей мамой. Пусть не только сегодняшний день - день твоего рождения, а и каждый твой день будет наполнен радостью!',
       'Мама! Это главный человек, который не предаст, не отвернется, даже если отвернуться все. Человек, который будет любить тебя всегда. Нежностью наполняется мое сердце, мама, когда я думаю, как много ты сделала для своих детей. Бессонные ночи у наших кроваток. Наши болезни. Наши успехи и неудачи, которые ты пропускала через свое сердце. Наша первая любовь, когда нам казалось, что весь мир рушится, но рядом с нами всегда была ты, и все становилось на свои места. Мы были настолько близки, что ты понимала нас без слов. В день твоего рождения я поздравляю тебя и низко кланяюсь. Искренне желаю, чтобы мелодия весны звучала в твоей душе всегда.',
       'Трудно подобрать те правильные слова, которые в полной мере смогли бы передать всю мою любовь к маме! Пусть Господь продлит твой жизненный век на долгие годы в здравии, благополучии, любви близких людей. Пусть печали, тревоги, болезни не знают пути к твоему порогу. Пусть двери твоего дома всегда будут распахнуты для хороших и добрых людей.',
       'Моя милая мама! Сегодня твой день рождения! Пусть побольше счастливых и приятных моментов дарит тебе жизнь. Пусть твоя жизнь будет озарена любовью и заботой твоей семьи. Ведь твоя любовь к нам, твоим детям, не знает границ. Мы ощущаем ее везде и всегда. А твои мудрые советы помогают нам преодолевать жизненные неурядицы. Мы привыкли видеть тебя веселой, жизнерадостной, оставайся такой всегда.',
       'Мама! В день, когда ты появилась на свет, на небе зажглась самая яркая звезда и стала неизменным спутником на твоем жизненном пути. У тебя столько жизнелюбия, столько позитивного отношения к жизни! Как здорово, что тебя не старят года! Ты энергична и молода душой, и я порой сомневаюсь, кто из нас старше? Общаясь с тобой, понимаешь, что жизнь - прекрасная штука! Живи долго и знай, что впереди у тебя много счастливых лет в кругу детей и внуков, искренне любящих тебя.',
       'Дорогая и любимая наша! Вот мы, твои дети, собрались здесь, чтоб отметить один прекраснейших дней в году. Хочется поблагодарить тебя за все, за все. Знай, наши успехи и достижения, в первую очередь, твоя заслуга, мама. Потому что ты с детства учила нас не стоять на месте, а двигаться вперед к цели, даже если тяжело, даже если никак. Желаем тебе постоянно быть такой же прекрасной, оптимистичной, доброй и внимательной.',
       'Родная моя мама! Так приятно смотреть на свое сияющее лицо и видеть, что у тебя прекрасно и чудесно. Пусть и в дальнейшем твое лицо будет озаряться только радостью и счастьем. Желаю тебе семейного благополучия, нереальных высот в профессии, настоящего уважения коллег, искренних и открытых душой людей на жизненном пути. Горжусь и люблю тебя.',
       'Твои объятия - самые теплые, твои руки – самые нежные, твое сердце – самое доброе! Спасибо тебе за это, моя родная! Как хорошо знать, что на свете есть мамочка, которая готова в любую минуту поддержать и помочь. Дорогая, я тебя не подведу и буду только радовать! Спасибо тебе за все! Исполнения всех заветных желаний и побольше поводов для улыбки!',
       'Проходят годы, а ты как и прежде светишься добротой и любовью, радо приглашаешь в свой дом и окружаешь заботой близких людей. Какое счастье, что ты – моя мама. Будь счастлива, моя родная и пусть никакие жизненные обстоятельства или препятствия не стоят на твоем пути, всюду сопутствует удача и успех.',
       'Мамочка – ты мой самый родной человек, ты всегда рядом и я мечтаю о том, чтобы это продлилось как можно дольше. В тебе столько доброты и искренности, силы и мужества, я желаю в твой день Рождения, чтобы с годами ты только приумножала свои духовные и материальные богатства. Пусть дети и внуки не расстраивают тебя, друзья почаще приходят к тебе в гости, а муж как и прежде смотрит на тебя с любовью и обожанием.',
       'Любимая мамочка! Ты – светлый человек, сильная и мудрая женщина, которая несмотря на удары судьбы всегда оставалась доброй и заботливой матерью, любящей женой и верным другом. Здоровья тебе, родная, а все остальное – благополучие, радость и счастье мы тебе обеспечим!',
       'С днем Рождения, дорогая мамочка! Спасибо за то, что всегда готова помочь и поддержать, накормить вкусным ужином и дать совет! Долгих тебе лет жизни, крепкого здоровья и самое главное – счастья!',
       'Мама, для меня ты самая родная на свете! С днем рождения! Будь всегда таким же замечательным человеком! Позволь пожелать тебе простого женского счастья. Ты знаешь, целой жизни вряд ли хватит, чтобы отблагодарить тебя за все, что ты сделала, да ты этого никогда и не просила. Пусть тебя всегда оберегает Господь, а по жизни сопутствует удача.',
       'Мама, с днем рождения! Пусть тебе сегодня улыбается солнце, пусть даже тень печали не коснется твоего лица! Всегда оставайся такой же открытой, красивой и доброй. Я знаю, что иногда огорчал тебя, но ты всегда меня прощала. Я никогда не забуду, как много ты для меня сделала, поэтому всегда буду рядом и обещаю помогать во всем.',
       'С днём рождения, милая мама! Ты всегда для меня стараешься, делаешь мою жизнь счастливой. Для тебя этот день не такой, как все, поэтому пусть сегодня у тебя будут только приятные неожиданности, пускай окружают тебя хорошие люди, а погода подарит тепло и свет. Я желаю тебе счастья, здоровья и долгих лет жизни! Я очень хочу, чтобы ты никогда не грустила!',
       'Мама, пусть твой день рождения принесёт тебе море прекрасного настроения. Пусть тебе ласково светит солнышко, пусть птицы поют свои весёлые песни. Я хочу поздравить тебя и пожелать оставаться всегда молодой и красивой. Спасибо тебе за заботу, полезные советы, душевную теплоту и счастье, которые ты даришь все эти годы.',
       'Милая моя мама! Поздравляю тебя с днем рождения! Я рад, что я твой сын и горжусь такой заботливой, надежной, любящей и всегда понимающей мамой. Желаю тебе, родная, долгих лет жизни, крепкого здоровья, жизнерадостности и везения! Пусть жизнь преподносит лишь приятные сюрпризы и счастливые мгновения!',
       'С днем рождения, моя родная, дорогая, любимая, самая лучшая мама! Я желаю тебе гармонии и здоровья, любви и радости, внимания близких и большой удачи на твоём пути. Я на весь мир в любую минуту готов заявить, что я — сын самой замечательной мамы на свете, и я всем сердцем желаю, чтобы ты, мамочка, всегда оставалась жизнерадостной и самой-самой счастливой!',
       'С огромной любовью в сердце поздравляю тебя, любимая мама, с днем рождения. Береги здоровье, живи долго-долго и будь счастлива!',
       'Поздравляю самую прекрасную, великолепную, роскошную, добрую, обворожительную, идеальную женщину. Все эти комплименты для тебя, мамочка! Ты заслуживаешь самых прекрасных слов и комплиментов, ты заслуживаешь, чтобы весь мир лежал у твоих ног. Я желаю, чтобы никакая грусть и печаль не смогла затмить красоты твоей улыбки и светящихся глаз. Чтобы твое здоровье никогда не пошатнулось и не приносило беспокойства. Пускай твое сердце только радуется и наслаждается светом, благополучием и покоем. С днем рождения!',
       'Родная, любимая, единственная моя мама! Прежде чем поздравить тебя с днем рождения, хочу попросить прощения. Я знаю, что ты много пережила и выстрадала из-за меня: бессонные ночи, тяжелые рабочие дни, седина в волосах, усталость в глазах, боль в теле и тревога в сердце. Спасибо, мамочка, что никогда не переставала меня любить. Пускай отныне твой и мой ангелы уносят твои заботы подальше от дома, привнося в душу спокойствие, а лицо твое всегда озаряет улыбка. Я люблю тебя, мамулечка.'
       ]  # 100 поздравлений


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,
                     "Моя фантастическая мамочка! Обычно, как только наступает знаменательный праздник, "
                     "именующийся днем рождения, в поздравлениях говорят "
                     "и пишут бесчисленное множество избитых "
                     "и не представляющих интереса вещей. "
                     "Я не буду опускаться до этого и просто скажу: спасибо, что ты есть!")  # приветсвие

    bot.send_message(message.chat.id,
                     "Это Бот которого написал Маруф. \n"
                     "Он сюда добавил много функций. \n"
                     "Чтобы узнать все эти функции, нажмите на /info")  # сообщение команды /start


@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id,
                     "Запустить бот: /start \n"
                     "Узнать информацию: /info \n"
                     "я вас люблю на 100 языках: /love \n"
                     "100 поздравлений с днем рождение: /birthday\n"
                     "20 ваших фотографий: /img")  # Комманда /info


@bot.message_handler(content_types=['text'], commands=['birthday'])
def birthday(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id,
                     f"{choice(brt)}  {choice(emoje)}")  # команда /birthday


@bot.message_handler(content_types=['text'], commands=['img'])
def img(message):
    bot.delete_message(message.chat.id, message.message_id)
    photo = open('media/' + random.choice(os.listdir('media')), 'rb')
    bot.send_photo(message.from_user.id, photo, f"{choice(emoje)}")  # команда /img


@bot.message_handler(content_types=['text'], commands=['love'])
def love(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id,
                     f"{choice(ilove)} {choice(emoje)}")  # комманда /love


print("Ехало")  # Значение бота вкл
bot.infinity_polling()  # Чтобы бот работал
