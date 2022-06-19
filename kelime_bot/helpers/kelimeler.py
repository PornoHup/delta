import random
kelimeler = ["gözəl ","bilmək ","sual","sağalmaq ","getmək","zaman","su","yarmaq","dəli","görmək",
             "yenidən", "çox", "fakt", "pul", "oynamaq", "çiçək", "şəhər", "yüksəlmək", "döyüş", "varlıq", "etmək",
             "güvən", "lazım", "müalicə", "bir", "rahat", "soyuq", "orası", "kitab", "paylaşmaq", "hesap", "bədən",
             "torpaq", "üzəri", "sistem", "xoş", "çəkilmək", "texnik", "yaxınlaşmaq", "il", "tarix", "kəsir", "bacı",
             "incə", "deyər", "oyda", "qarşılıql","vermək", "sahib", "artıq", "kişi", "diyar", "dönəm", "yenə", "bunlar",
             "kitab", "xəta", "tapmaq", "siz", "dövlət", "qabaq", "enerji", "baxmaq", "ütünə", "oyun", "baş", "başlamaq",
             "tutmaq", "birbiri", "heçbir", "yatmaq", "su", "ürək", "hal", "doğru", "orta", "başqa", "böyük", "etmək",
             "yeni", "çoxlu", "soruşmaq", "onlar", "açmaq", "hem", "həb", "səs", "ağlamaq", "dəli", "saat", "hasil",
             'bir', 'veteran', 'olmak', 'bu', 'içki', 'onuncu', 'ben', 'demək', 'çox', 'yaşıl', 'ana', 'kimi', 'daha', 'almaq',
             'var', 'özün', 'gəlmək', 'ilə', 'vermək', 'baba', 'sonra', 'qədir', 'yer', 'ata', 'insan', 'deyil', 'hər',
             'istemek', 'yıl', 'çıkmak', 'görmək', 'gün', 'biz', 'getmkə', 'iş', 'şey', 'axtarmaq', 'iki', 'bilmək', 'əl', 'zaman',
             'ya', 'çocuk', 'iki', 'baxmakq', 'çalışmak', 'içində', 'böyük', 'yox', 'başlamaq', 'yol', 'kalmak', 'neden', 'siz',
             'konu', 'yaradmaq', 'yaxşı', 'qadın', 'evli', 'demək', 'bulunmak', 'söylemek', 'göz', 'gerekmek', 'dünya',
             'baş', 'vaxt', 'yan', 'getmək', 'sən', 'onlar', 'yeni', 'öncə', 'başqa', 'hal', 'orta', 'su', 'girmek', 'ülke',
             'yemek', 'heçnə', 'oxumaq', 'necə', 'bütün', 'qarşı', 'tapmaq', 'evvli', 'yaşamak', 'düşünmek', 'aynı', 'iç', 'ancaq',
             'kişi', 'bunlar', 'veya', 'ilk', 'göre', 'qabaq', 'son', 'biri', 'şəkil', 'önemli', 'yüz', 'hem', 'göstərmək', 'etmək',
             'alt', 'gətirmək', 'işlətmək', 'çünkü', 'tərəf', 'kimdi', 'adam', 'onun', 'diğer', 'artık', 'üzerinde', 'səs', 'hep',
             'doğru', 'dayanmaq', 'kız', 'tüm', 'çekmek', 'konuşmak', 'pullu', 'anlamak', 'anne', 'az', 'bazı', 'baba', 'hayat',
             'sadece', 'balaca', 'çox', 'bilgi', 'an', 'soruşma', 'bunun', 'öyle', 'yine', 'sağlamak', 'sonuç', 'kullanılmak', 'dış',
             'ad', 'yani', 'süre', 'dönmek', 'açmak', 'oturmak', 'anlatmak', 'bırakmak', 'hemen', 'saat', 'yaş', 'sorun', 'devlet',
             'sahip', 'sıra', 'yazmak', 'yüzde', 'ay', 'atmak', 'tutmak', 'bunu', 'olay', 'düşmek', 'duymak', 'söz', 'güzel',
             'sevmek', 'biraz', 'zor', 'çıkarmak', 'şu', 'koymak', 'tek', 'sistem', 'birlikte', 'verilmek', 'kim', 'alınmak', 'genç',
             'kapı', 'kitap', 'üzerine', 'burada', 'gece', 'alan', 'birbiri', 'işte', 'beklemek', 'uzun', 'hiçbir', 'bugün', 'dönem',
             'arkadaş', 'ürün', 'aile', 'üç', 'okumak', 'erkek', 'hərkəs', 'güc', 'bəlmək', 'doğru', 'tam', 'gecə', 'Riyad',
             'çevrə', 'köhnə', 'zəng', 'yaşma', 'əhali', 'yaxın', 'yol', 'bəy', 'tarix', 'özellik', 'bölüm', 'şəxsi', 'ağıl',
             'kimsə', 'pak', 'eğer', 'gerek', 'yaxın', 'anlamaq', 'yüksek', 'banka', 'kez', 'ayak', 'daşımaq', 'geri', 'toplu',
             'maşın', 'maddə', 'türk', 'qəlyan', 'görüldü', 'hava', 'sayı', 'farklı', 'grup', 'otaq', 'bacı', 'dolmaq', 'xəbər',
             'allah', 'ayrıca', 'gələn', 'çin', 'sual', 'arxa', 'qazanmaq', 'yazı', 'dərs', 'açıq', 'öyrənmək', 'sürmək',
             'dil', 'şirket', 'kaynak', 'bitmək', 'program', 'devametmek', 'hareket', 'rəng', 'açılmaq', 'hak', 'inanmaq',
             'çalmaq', 'acı', 'parça', 'gazete', 'yaratmaq', 'yaxşı', 'dəyər', 'tanımaq', 'yapı', 'doktor', 'gəlir',
             'hərbiçi', 'amaç', 'bölge', 'film', 'üzere', 'müşteri', 'zaten', 'telefon', 'eğitim', 'deniz', 'ikinci',
             'qalxmaq', 'hatta', 'etki', 'gelir', 'keçən', 'bel', 'düşünce', 'milyon', 'oynamak', 'dəyişmək', 'tütün',
             'yaratmaq', 'xal', 'sanmak', 'geçirmek', 'söyüş', 'kurmak', 'fakat', 'buna', 'resim', 'ışıq', 'içmək',
             'xanım', 'xəstə', 'ehtiyac', 'nöktə', 'yönlü', 'xəta', 'oyun', 'artmak', 'yeniden', 'işlem', 'kısa', 'kolay',
             'hal', 'qan', 'aslında', 'ağıl', 'orada', 'dikkat', 'uzaq', 'bilgisayar', 'gələcək', 'görünmek',
             'şəkil', 'oğul', 'dinlemek', 'uyğun', 'manat', 'passiv', 'dakika', 'unutmak', 'yürümek', 'böylece', 'kötü',
             'maşın', 'ağız', 'duygu', 'uygulamak', 'hâlâ', 'örnek', 'birçok', 'izlemek', 'derece', 'mümkün', 'şöyle',
             'duvar', 'on', 'sənə', 'ana', 'hastalık', 'öğrenci', 'televizyon', 'yöntem', 'masa', 'ölmek', 'takım', 'üst',
             'baş', 'müzik', 'ayrılmak', 'enerji', 'üniversite', 'spor', 'türlü', 'can', 'rağmen', 'kısım', 'ölüm',
             'süretli', 'sağlıq', 'çeşitli', 'bundan', 'hissetmek', 'oysa', 'sabah', 'internet', 'teknik', 'dışarı',
             'mərkəz', 'orta', 'yerinə', 'düz', 'kənd', 'yorulmaq', 'aşağı', 'cevap', 'yatmak', 'toprak', '', 'akşam',
             'sarı', 'götürmek', 'katılmak', 'yoksa', 'qurmaq', 'ödemek', 'sanki', 'kan', 'hasta', 'şehir', 'inmek',
             'qara', 'bilinmek', 'həftə', 'lənpə', 'hesab', 'otomobil', 'yabancı', 'davranış', 'mutfak', 'kent', 'bazen',
             'vacib', 'ayrı', 'qiymət', 'hakkında', 'qaldırmaq', 'kol', 'tək', 'hazırlamaq', 'cam', 'sonunda', 'yavaş',
             'lazım', 'önem', 'arvad', 'yanlış', 'varlı', 'tar', 'arı', 'təkcə', 'satış', 'içeri', 'doğal', 'sahipolmak',
             'ekonomi', 'acı', 'xeyir', 'qorumaq', 'qat', 'ekonomi', 'genel', 'bildirmək', 'fotoğraf', 'hayvan', 'savaş',
             'yumurta', 'aşırı', 'eylem', 'istəmək', 'kərim', 'kriz', 'birlik',
             'qapanmaq'
             ]


def kelime_sec():
    return random.choice(kelimeler)
