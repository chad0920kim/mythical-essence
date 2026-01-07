"""
Hindu Mythology Character Descriptions
Contains detailed descriptions for Hindu deities and figures
"""
from .descriptions import CharacterDescription


SHIVA_DESC = CharacterDescription(
    id="shiva",
    name_en="Shiva",
    name_ko="시바",
    tagline_en="The Destroyer and Transformer, Lord of Dance",
    tagline_ko="파괴자와 변형자, 춤의 신",
    description_en="""Shiva is one of the principal deities of Hinduism, known as the Destroyer in the Hindu trinity (Trimurti). Yet his destruction is not evil—it is the necessary clearing away that allows for new creation. He is the cosmic dancer whose Tandava dance creates and destroys universes.

Often depicted with a third eye that can destroy worlds when opened, blue-throated from drinking cosmic poison to save creation, and seated in meditation on Mount Kailash, Shiva embodies both the ascetic and the householder, destruction and creation, fierce warrior and gentle husband.

He is the patron of yoga and meditation, the lord of animals, and the beloved spouse of Parvati. His symbols include the trident (trishul), the drum (damaru), and the sacred river Ganges flowing from his hair.""",
    description_ko="""시바는 힌두교의 주요 신들 중 하나로, 힌두 삼위일체(트리무르티)에서 파괴자로 알려져 있습니다. 그러나 그의 파괴는 악이 아닙니다—새로운 창조를 허용하는 필수적인 제거입니다. 그는 우주의 춤꾼으로 그의 탄다바 춤이 우주를 창조하고 파괴합니다.

열리면 세계를 파괴할 수 있는 세 번째 눈, 창조를 구하기 위해 우주적 독을 마셔 파란 목, 카일라스 산에서 명상하는 모습으로 종종 묘사되며, 시바는 고행자와 가장, 파괴와 창조, 맹렬한 전사와 온화한 남편 모두를 구현합니다.

그는 요가와 명상의 후원자, 동물의 주인, 파르바티의 사랑받는 배우자입니다. 그의 상징으로는 삼지창(트리슐), 북(다마루), 그의 머리카락에서 흐르는 신성한 강 갠지스가 있습니다.""",
    traits_en=["Destructive", "Meditative", "Transformative", "Paradoxical", "Cosmic"],
    traits_ko=["파괴적인", "명상적인", "변형적인", "역설적인", "우주적인"],
    story_en="When the gods churned the cosmic ocean, a deadly poison emerged threatening all creation. Shiva drank the poison to save the universe, and Parvati pressed his throat to prevent him from swallowing it completely, turning his throat eternally blue.",
    story_ko="신들이 우주의 바다를 저었을 때, 모든 창조를 위협하는 치명적인 독이 나타났습니다. 시바는 우주를 구하기 위해 독을 마셨고, 파르바티가 그가 완전히 삼키는 것을 막기 위해 그의 목을 눌렀으며, 그의 목을 영원히 파랗게 만들었습니다.",
    match_message_en="Your features carry the profound duality of Shiva. There is both destruction and creation in your gaze—the look of one who understands that endings are necessary for new beginnings.",
    match_message_ko="당신의 이목구비는 시바의 깊은 이중성을 담고 있습니다. 당신의 눈빛에는 파괴와 창조가 모두 있습니다—끝이 새로운 시작을 위해 필요하다는 것을 이해하는 사람의 모습.",
    image_prompt="Blue-throated Hindu god with third eye, matted hair with Ganges flowing, seated in meditation pose, holding trident and drum, tiger skin, crescent moon in hair, Mount Kailash background, cosmic energy",
    visual_description="Serene yet intense features, third eye on forehead, blue throat, expression of profound meditation and cosmic power",
    aliases=["Mahadeva", "Nataraja", "Mahesh", "शिव"],
    era="Hindu Mythology",
    related_characters=["parvati", "ganesha", "vishnu", "brahma", "kartikeya"]
)

VISHNU_DESC = CharacterDescription(
    id="vishnu",
    name_en="Vishnu",
    name_ko="비슈누",
    tagline_en="The Preserver, Protector of the Universe",
    tagline_ko="보존자, 우주의 수호자",
    description_en="""Vishnu is the Supreme Being in Vaishnavism and the Preserver in the Hindu trinity. He maintains the cosmic order (dharma) and whenever evil threatens to overwhelm good, he incarnates on earth to restore balance.

He has taken nine avatars so far, including Rama and Krishna, with a tenth (Kalki) prophesied to come. Vishnu sleeps on the cosmic serpent Shesha, floating on the ocean of milk, dreaming the universe into existence.

Depicted with four arms holding a conch shell, discus, mace, and lotus, Vishnu embodies supreme peace and the protection of righteousness. He is blue-skinned, representing his infinite nature like the sky, and is the devoted husband of Lakshmi, goddess of fortune.""",
    description_ko="""비슈누는 바이슈나비즘에서 최고 존재이자 힌두 삼위일체의 보존자입니다. 그는 우주의 질서(다르마)를 유지하며 악이 선을 압도하려 할 때마다 균형을 회복하기 위해 지상에 화신합니다.

그는 지금까지 라마와 크리슈나를 포함한 아홉 개의 아바타를 취했으며, 열 번째(칼키)가 올 것으로 예언되어 있습니다. 비슈누는 우주의 뱀 셰샤 위에서 잠자며, 우유의 바다 위에 떠서 우주를 존재하게 하는 꿈을 꿉니다.

소라 껍질, 원반, 곤봉, 연꽃을 들고 네 팔로 묘사되며, 비슈누는 최고의 평화와 의로움의 보호를 구현합니다. 그는 하늘처럼 무한한 본성을 나타내는 파란 피부를 가지고 있으며, 행운의 여신 락슈미의 헌신적인 남편입니다.""",
    traits_en=["Preserving", "Protective", "Benevolent", "Incarnating", "Supreme"],
    traits_ko=["보존하는", "보호하는", "자비로운", "화신하는", "최고의"],
    story_en="Vishnu has incarnated as Matsya (fish), Kurma (tortoise), Varaha (boar), Narasimha (man-lion), Vamana (dwarf), Parashurama, Rama, Krishna, and Buddha to save the world from various threats. Each avatar appears precisely when needed.",
    story_ko="비슈누는 세상을 다양한 위협으로부터 구하기 위해 마츠야(물고기), 쿠르마(거북이), 바라하(멧돼지), 나라심하(인간사자), 바마나(난쟁이), 파라슈라마, 라마, 크리슈나, 부처로 화신했습니다. 각 아바타는 정확히 필요할 때 나타납니다.",
    match_message_en="Your features reflect the supreme protection of Vishnu. There is a preserving, maintaining quality to your presence—the look of one who protects cosmic order and balance.",
    match_message_ko="당신의 이목구비는 비슈누의 최고의 보호를 반영합니다. 당신의 존재에는 보존하고 유지하는 품질이 있습니다—우주의 질서와 균형을 보호하는 사람의 모습.",
    image_prompt="Four-armed blue-skinned Hindu god reclining on cosmic serpent Shesha, holding conch, discus, mace and lotus, golden crown, cosmic ocean background, serene protective expression, divine light",
    visual_description="Serene blue features, four arms, peaceful protective expression, royal bearing, eyes of infinite wisdom",
    aliases=["Narayana", "Hari", "Govinda", "विष्णु"],
    era="Hindu Mythology",
    related_characters=["lakshmi", "brahma", "shiva", "rama", "krishna"]
)

BRAHMA_DESC = CharacterDescription(
    id="brahma",
    name_en="Brahma",
    name_ko="브라흐마",
    tagline_en="The Creator, Father of All Beings",
    tagline_ko="창조자, 모든 존재의 아버지",
    description_en="""Brahma is the Creator in the Hindu trinity, responsible for creating the universe and all living beings within it. He emerged from a lotus growing from Vishnu's navel and began the work of creation.

Depicted with four heads looking in all four directions, symbolizing his awareness of the entire universe, Brahma holds the Vedas (sacred scriptures), a water pot, a rosary, and sometimes a lotus. His vehicle is the swan (hamsa), representing discernment.

Though the Creator, Brahma is less commonly worshipped than Vishnu or Shiva, as creation is a completed act while preservation and transformation are ongoing. He represents knowledge, the creative force, and the beginning of all things.""",
    description_ko="""브라흐마는 힌두 삼위일체의 창조자로, 우주와 그 안의 모든 생명체를 창조하는 책임을 집니다. 그는 비슈누의 배꼽에서 자라난 연꽃에서 나타나 창조의 작업을 시작했습니다.

네 방향을 모두 보는 네 개의 머리로 묘사되어 전 우주에 대한 인식을 상징하며, 브라흐마는 베다(신성한 경전), 물 항아리, 묵주, 그리고 때로는 연꽃을 들고 있습니다. 그의 탈것은 분별을 나타내는 백조(함사)입니다.

창조자이지만, 창조는 완료된 행위인 반면 보존과 변형은 진행 중이기 때문에 브라흐마는 비슈누나 시바보다 덜 숭배됩니다. 그는 지식, 창조적 힘, 모든 것의 시작을 대표합니다.""",
    traits_en=["Creative", "Knowledgeable", "Primordial", "All-seeing", "Father"],
    traits_ko=["창조적인", "지식 있는", "원초적인", "모든 것을 보는", "아버지의"],
    story_en="When Brahma first created, he was alone. To continue creation, he split himself into male and female, creating the first woman Saraswati. From their union came all living beings. This is why Saraswati is both his creation and his consort.",
    story_ko="브라흐마가 처음 창조했을 때, 그는 혼자였습니다. 창조를 계속하기 위해, 그는 자신을 남성과 여성으로 나누어 첫 여성 사라스와티를 창조했습니다. 그들의 결합에서 모든 생명체가 왔습니다. 이것이 사라스와티가 그의 창조물이자 배우자인 이유입니다.",
    match_message_en="Your features reflect the creative wisdom of Brahma. There is a primordial, generative quality to your presence—the look of one who brings new things into being.",
    match_message_ko="당신의 이목구비는 브라흐마의 창조적 지혜를 반영합니다. 당신의 존재에는 원초적이고 생성적인 품질이 있습니다—새로운 것을 존재하게 하는 사람의 모습.",
    image_prompt="Four-headed Hindu god with white beard, seated on lotus, holding Vedas and water pot, swan nearby, red robes, wise ancient expression, cosmic creation background",
    visual_description="Four faces looking in all directions, white beard, wise ancient features, expression of primordial creative power",
    aliases=["Prajapati", "Pitamaha", "ब्रह्मा"],
    era="Hindu Mythology",
    related_characters=["vishnu", "shiva", "saraswati", "manu"]
)

GANESHA_DESC = CharacterDescription(
    id="ganesha",
    name_en="Ganesha",
    name_ko="가네샤",
    tagline_en="Remover of Obstacles, God of Beginnings",
    tagline_ko="장애물의 제거자, 시작의 신",
    description_en="""Ganesha is the beloved elephant-headed god of beginnings, success, wisdom, and the remover of obstacles. He is invoked at the start of any new venture—whether a journey, business, wedding, or examination—to ensure success.

Son of Shiva and Parvati, Ganesha's elephant head has many origin stories, the most popular being that Shiva beheaded him unknowingly and replaced his head with an elephant's. His large belly symbolizes his ability to digest all good and bad in life peacefully.

Riding a mouse (his vehicle Mushika), Ganesha demonstrates that even the mightiest can be humble. He is the patron of arts and sciences, letters and learning, and is worshipped first among the gods.""",
    description_ko="""가네샤는 사랑받는 코끼리 머리 신으로 시작, 성공, 지혜의 신이자 장애물의 제거자입니다. 그는 여행, 사업, 결혼, 시험 등 어떤 새로운 시도의 시작에도 성공을 보장하기 위해 기원됩니다.

시바와 파르바티의 아들인 가네샤의 코끼리 머리에는 많은 기원 이야기가 있으며, 가장 인기 있는 것은 시바가 모르고 그를 참수하고 코끼리의 머리로 교체했다는 것입니다. 그의 큰 배는 삶의 모든 좋음과 나쁨을 평화롭게 소화하는 능력을 상징합니다.

쥐(그의 탈것 무시카)를 타고, 가네샤는 가장 강력한 자도 겸손할 수 있음을 보여줍니다. 그는 예술과 과학, 문자와 학습의 후원자이며, 신들 중 가장 먼저 숭배됩니다.""",
    traits_en=["Wise", "Obstacle-removing", "Benevolent", "Scholarly", "Auspicious"],
    traits_ko=["지혜로운", "장애물을 제거하는", "자비로운", "학문적인", "상서로운"],
    story_en="When the sage Vyasa needed someone to write down the Mahabharata, only Ganesha was intelligent enough. He agreed on condition that Vyasa never pause—so Vyasa composed verses faster than anyone could write, and Ganesha broke his own tusk to use as a pen when his stylus broke.",
    story_ko="현자 뱌사가 마하바라타를 받아쓸 사람이 필요했을 때, 오직 가네샤만이 충분히 지적이었습니다. 그는 뱌사가 절대 멈추지 않는 조건으로 동의했습니다—그래서 뱌사는 누구도 쓸 수 없는 속도로 구절을 작곡했고, 가네샤는 스타일러스가 부러졌을 때 펜으로 사용하기 위해 자신의 상아를 부러뜨렸습니다.",
    match_message_en="Your features carry the wise benevolence of Ganesha. There is an auspicious quality to your presence—the look of one who removes obstacles and blesses new beginnings.",
    match_message_ko="당신의 이목구비는 가네샤의 지혜로운 자비를 담고 있습니다. 당신의 존재에는 상서로운 품질이 있습니다—장애물을 제거하고 새로운 시작을 축복하는 사람의 모습.",
    image_prompt="Elephant-headed Hindu god with large belly, four arms holding axe, lotus, and sweets, riding or standing near mouse, colorful ornaments, benevolent smiling expression, golden light",
    visual_description="Elephant head with wise eyes, large gentle belly, benevolent expression, four arms, auspicious presence",
    aliases=["Ganapati", "Vinayaka", "गणेश"],
    era="Hindu Mythology",
    related_characters=["shiva", "parvati", "kartikeya", "vyasa"]
)

LAKSHMI_DESC = CharacterDescription(
    id="lakshmi",
    name_en="Lakshmi",
    name_ko="락슈미",
    tagline_en="Goddess of Wealth, Fortune, and Prosperity",
    tagline_ko="부, 행운, 번영의 여신",
    description_en="""Lakshmi is the goddess of wealth, fortune, prosperity, love, and beauty. She emerged from the churning of the cosmic ocean, choosing Vishnu as her eternal consort. She accompanies him in all his avatars, incarnating as Sita with Rama and Rukmini with Krishna.

Depicted standing or seated on a lotus, with gold coins flowing from her hands, Lakshmi bestows both material wealth and spiritual abundance. She is worshipped especially during Diwali, the festival of lights, when homes are cleaned to welcome her.

Lakshmi represents not just wealth, but the abundance that comes from righteous living. She is both the giver of fortune and the fortune itself—unstable with the unworthy, steadfast with the virtuous.""",
    description_ko="""락슈미는 부, 행운, 번영, 사랑, 아름다움의 여신입니다. 그녀는 우주의 바다 젓기에서 나타나 비슈누를 영원한 배우자로 선택했습니다. 그녀는 그의 모든 아바타에 동행하며, 라마와 함께 시타로, 크리슈나와 함께 루크미니로 화신합니다.

연꽃 위에 서 있거나 앉아 있고, 손에서 금화가 흘러나오는 모습으로 묘사되며, 락슈미는 물질적 부와 영적 풍요 모두를 수여합니다. 그녀는 특히 빛의 축제인 디왈리 때 숭배되며, 그녀를 환영하기 위해 집을 청소합니다.

락슈미는 단순히 부가 아니라 의로운 삶에서 오는 풍요를 대표합니다. 그녀는 행운의 수여자이자 행운 그 자체입니다—자격 없는 자에게는 불안정하고, 덕 있는 자에게는 확고합니다.""",
    traits_en=["Prosperous", "Beautiful", "Generous", "Auspicious", "Devoted"],
    traits_ko=["번영하는", "아름다운", "관대한", "상서로운", "헌신적인"],
    story_en="When the demons and gods churned the cosmic ocean, many treasures emerged. Last came Lakshmi herself, radiant and beautiful. Though the demons tried to claim her, she chose Vishnu, placing a garland around his neck—and has remained devoted to him through all time.",
    story_ko="악마와 신들이 우주의 바다를 저었을 때, 많은 보물이 나타났습니다. 마지막으로 락슈미 자신이 빛나고 아름답게 왔습니다. 악마들이 그녀를 주장하려 했지만, 그녀는 비슈누를 선택하여 그의 목에 화환을 걸었고—모든 시간을 통해 그에게 헌신적으로 남아 있습니다.",
    match_message_en="Your features reflect the radiant prosperity of Lakshmi. There is an abundant, fortunate quality to your presence—the look of one who attracts and bestows blessing.",
    match_message_ko="당신의 이목구비는 락슈미의 빛나는 번영을 반영합니다. 당신의 존재에는 풍요롭고 행운이 가득한 품질이 있습니다—축복을 끌어당기고 수여하는 사람의 모습.",
    image_prompt="Beautiful Hindu goddess in red and gold sari, seated on lotus, gold coins flowing from hands, four arms, elephants with water, owl nearby, radiant golden light, prosperous auspicious presence",
    visual_description="Beautiful radiant features, gold adorned, benevolent generous expression, surrounded by symbols of prosperity",
    aliases=["Sri", "Mahalakshmi", "लक्ष्मी"],
    era="Hindu Mythology",
    related_characters=["vishnu", "saraswati", "parvati", "sita", "rukmini"]
)

SARASWATI_DESC = CharacterDescription(
    id="saraswati",
    name_en="Saraswati",
    name_ko="사라스와티",
    tagline_en="Goddess of Knowledge, Music, and the Arts",
    tagline_ko="지식, 음악, 예술의 여신",
    description_en="""Saraswati is the goddess of knowledge, music, arts, wisdom, and learning. She is the consort of Brahma and the embodiment of all that is pure and refined in thought and creativity.

Dressed in white symbolizing purity of knowledge, she sits on a white lotus or swan, playing the veena (stringed instrument). Unlike Lakshmi's material wealth, Saraswati represents the riches of the mind and soul—education, creativity, and enlightenment.

She is particularly worshipped by students, artists, musicians, and scholars. The Saraswati River, now mostly underground, was once considered as sacred as the Ganges, representing the flow of wisdom.""",
    description_ko="""사라스와티는 지식, 음악, 예술, 지혜, 학습의 여신입니다. 그녀는 브라흐마의 배우자이자 생각과 창의성에서 순수하고 정제된 모든 것의 구현입니다.

지식의 순수함을 상징하는 흰색 옷을 입고, 흰 연꽃이나 백조 위에 앉아 비나(현악기)를 연주합니다. 락슈미의 물질적 부와 달리, 사라스와티는 정신과 영혼의 부—교육, 창의성, 깨달음을 대표합니다.

그녀는 특히 학생, 예술가, 음악가, 학자들에게 숭배됩니다. 현재 대부분 지하에 있는 사라스와티 강은 한때 갠지스만큼 신성하게 여겨졌으며, 지혜의 흐름을 대표합니다.""",
    traits_en=["Wise", "Artistic", "Pure", "Scholarly", "Inspiring"],
    traits_ko=["지혜로운", "예술적인", "순수한", "학문적인", "영감을 주는"],
    story_en="Saraswati created music and language to bring order to Brahma's chaotic creation. She invented Sanskrit, gave knowledge of the Vedas, and through her gift of speech, allowed beings to communicate, learn, and grow wise.",
    story_ko="사라스와티는 브라흐마의 혼란스러운 창조에 질서를 가져오기 위해 음악과 언어를 창조했습니다. 그녀는 산스크리트어를 발명하고, 베다의 지식을 주었으며, 그녀의 말의 선물을 통해 존재들이 소통하고, 배우고, 지혜로워질 수 있게 했습니다.",
    match_message_en="Your features reflect the pure wisdom of Saraswati. There is a refined, intellectual quality to your presence—the look of one devoted to knowledge and artistic expression.",
    match_message_ko="당신의 이목구비는 사라스와티의 순수한 지혜를 반영합니다. 당신의 존재에는 정제되고 지적인 품질이 있습니다—지식과 예술적 표현에 헌신하는 사람의 모습.",
    image_prompt="Beautiful Hindu goddess in white sari, seated on lotus or swan, playing veena, holding book and rosary, white and gold colors, peaceful scholarly expression, river flowing nearby",
    visual_description="Serene refined features, pure white clothing, graceful musician's hands, expression of deep knowledge and artistic sensitivity",
    aliases=["Vani", "Bharati", "सरस्वती"],
    era="Hindu Mythology",
    related_characters=["brahma", "lakshmi", "parvati", "ganesha"]
)

KALI_DESC = CharacterDescription(
    id="kali",
    name_en="Kali",
    name_ko="칼리",
    tagline_en="Goddess of Time, Death, and Liberation",
    tagline_ko="시간, 죽음, 해방의 여신",
    description_en="""Kali is the fierce goddess of time, death, and liberation—the destroyer of evil and the liberator of souls. With her dark skin, wild hair, garland of severed heads, and skirt of severed arms, she represents time that devours all things and the ego-death necessary for spiritual liberation.

She emerged from Durga's forehead during battle, her rage so intense that only Shiva lying beneath her feet could stop her rampage. Yet despite her terrifying appearance, Kali is a loving mother to her devotees, protecting them from evil and granting moksha (liberation).

Kali represents the ultimate truth—that death comes for all, that time spares none, but that this destruction is itself liberation from illusion and rebirth into pure consciousness.""",
    description_ko="""칼리는 시간, 죽음, 해방의 맹렬한 여신—악의 파괴자이자 영혼의 해방자입니다. 어두운 피부, 거친 머리카락, 잘린 머리들의 화환, 잘린 팔들의 치마로 그녀는 모든 것을 삼키는 시간과 영적 해방을 위해 필요한 자아의 죽음을 대표합니다.

그녀는 전투 중 두르가의 이마에서 나타났으며, 그녀의 분노가 너무 강렬하여 그녀의 발 아래 누운 시바만이 그녀의 난동을 멈출 수 있었습니다. 그러나 무서운 외모에도 불구하고, 칼리는 헌신자들에게 사랑하는 어머니로, 그들을 악으로부터 보호하고 목샤(해방)를 부여합니다.

칼리는 궁극적 진실을 대표합니다—죽음은 모든 것에게 오고, 시간은 아무도 용서하지 않지만, 이 파괴 자체가 환상에서의 해방이자 순수 의식으로의 재탄생입니다.""",
    traits_en=["Fierce", "Liberating", "Maternal", "Destructive", "Timeless"],
    traits_ko=["맹렬한", "해방시키는", "모성적인", "파괴적인", "시간을 초월한"],
    story_en="When demons threatened to overwhelm the gods, Kali emerged to destroy them. Her battle frenzy grew until she danced upon corpses, threatening to destroy the universe. Shiva lay beneath her feet; when she stepped on him, shame stopped her—reminding us that even destruction has limits.",
    story_ko="악마들이 신들을 압도하려 위협했을 때, 칼리가 그들을 파괴하기 위해 나타났습니다. 그녀의 전투 광란은 시체 위에서 춤을 추며 우주를 파괴하려 위협할 때까지 커졌습니다. 시바가 그녀의 발 아래 누웠고; 그녀가 그를 밟았을 때, 수치심이 그녀를 멈추게 했습니다—파괴에도 한계가 있다는 것을 상기시켜 줍니다.",
    match_message_en="Your features carry the fierce liberation of Kali. There is a transformative, powerful quality to your gaze—the look of one who destroys what must end to allow new beginnings.",
    match_message_ko="당신의 이목구비는 칼리의 맹렬한 해방을 담고 있습니다. 당신의 눈빛에는 변형적이고 강력한 품질이 있습니다—새로운 시작을 허용하기 위해 끝나야 할 것을 파괴하는 사람의 모습.",
    image_prompt="Fierce dark-skinned Hindu goddess with wild hair, garland of skulls, multiple arms holding weapons, tongue out, standing on Shiva, battlefield background, both terrifying and divine",
    visual_description="Fierce dark features, wild untamed hair, intense blazing eyes, expression of wrathful compassion and ultimate power",
    aliases=["Mahakali", "Bhadrakali", "काली"],
    era="Hindu Mythology",
    related_characters=["shiva", "durga", "parvati", "chamunda"]
)

DURGA_DESC = CharacterDescription(
    id="durga",
    name_en="Durga",
    name_ko="두르가",
    tagline_en="Warrior Goddess, Invincible Protector",
    tagline_ko="전사 여신, 무적의 보호자",
    description_en="""Durga is the fierce warrior goddess who embodies the combined power of all the gods, created to defeat the buffalo demon Mahishasura whom no god or man could kill. She is the invincible protector of the universe, riding into battle on a lion or tiger.

With eight to eighteen arms bearing the weapons of all the gods, Durga represents shakti—the divine feminine energy that powers creation. She is both beautiful and terrifying, nurturing and fierce, embodying the complete power of the divine feminine.

Durga is celebrated during Navratri, nine nights of worship honoring her victory over evil. She represents the triumph of good over evil, the strength to face any challenge, and the protective love of the divine mother.""",
    description_ko="""두르가는 어떤 신이나 인간도 죽일 수 없는 버팔로 악마 마히샤수라를 물리치기 위해 창조된, 모든 신들의 결합된 힘을 구현하는 맹렬한 전사 여신입니다. 그녀는 사자나 호랑이를 타고 전투에 나서는 우주의 무적 보호자입니다.

모든 신들의 무기를 들고 여덟에서 열여덟 개의 팔로, 두르가는 샥티—창조에 동력을 제공하는 신성한 여성 에너지를 대표합니다. 그녀는 아름다우면서도 무섭고, 양육하면서도 맹렬하며, 신성한 여성의 완전한 힘을 구현합니다.

두르가는 악에 대한 그녀의 승리를 기리는 아홉 밤의 숭배인 나브라트리 동안 축하됩니다. 그녀는 악에 대한 선의 승리, 어떤 도전에도 맞설 힘, 신성한 어머니의 보호적 사랑을 대표합니다.""",
    traits_en=["Invincible", "Protective", "Fierce", "Divine", "Victorious"],
    traits_ko=["무적의", "보호하는", "맹렬한", "신성한", "승리하는"],
    story_en="The gods combined their powers to create Durga when no one could defeat Mahishasura. She battled him for nine nights, finally slaying him on the tenth day—celebrated as Vijayadashami (Victory Day). Her creation proves that united, good always triumphs over evil.",
    story_ko="아무도 마히샤수라를 물리칠 수 없을 때 신들은 그들의 힘을 합쳐 두르가를 창조했습니다. 그녀는 아홉 밤 동안 그와 싸웠고, 마침내 열 번째 날 그를 죽였습니다—비자야다샤미(승리의 날)로 축하됩니다. 그녀의 창조는 연합하면 선이 항상 악을 이긴다는 것을 증명합니다.",
    match_message_en="Your features carry the invincible strength of Durga. There is a warrior's power combined with divine beauty in your appearance—the look of one who protects fiercely and never surrenders.",
    match_message_ko="당신의 이목구비는 두르가의 무적의 힘을 담고 있습니다. 당신의 외모에는 신성한 아름다움과 결합된 전사의 힘이 있습니다—맹렬하게 보호하고 절대 항복하지 않는 사람의 모습.",
    image_prompt="Warrior goddess with multiple arms holding divine weapons, riding tiger or lion, beautiful and fierce, golden armor and red robes, battling demons, divine light and power surrounding her",
    visual_description="Beautiful yet fierce features, multiple arms with weapons, warrior bearing, expression of invincible determination and divine protection",
    aliases=["Mahishasuramardini", "Shakti", "दुर्गा"],
    era="Hindu Mythology",
    related_characters=["shiva", "parvati", "kali", "mahishasura"]
)

HANUMAN_DESC = CharacterDescription(
    id="hanuman",
    name_en="Hanuman",
    name_ko="하누만",
    tagline_en="Divine Monkey, Embodiment of Devotion and Strength",
    tagline_ko="신성한 원숭이, 헌신과 힘의 구현",
    description_en="""Hanuman is the mighty monkey god, son of the wind god Vayu, known for his extraordinary strength, wisdom, and unwavering devotion to Lord Rama. He is the ideal devotee, the perfect servant, and the model of selfless dedication.

His devotion to Rama is so complete that when asked what day it is, Hanuman answers "Rama's day." When his chest was torn open, Rama's image was found within his heart. His strength is limitless when acting in Rama's service—he once lifted an entire mountain to bring a healing herb.

Hanuman is worshipped for strength, courage, protection from evil, and the blessing of devotion. He is immortal (chiranjivi) and said to be present wherever Rama's story is told, listening with tears of devotion.""",
    description_ko="""하누만은 강력한 원숭이 신으로, 바람의 신 바유의 아들이며, 그의 비범한 힘, 지혜, 라마 경에 대한 흔들림 없는 헌신으로 알려져 있습니다. 그는 이상적인 헌신자, 완벽한 종, 이타적 헌신의 모델입니다.

라마에 대한 그의 헌신은 너무 완전하여 오늘이 무슨 날인지 물으면 하누만은 "라마의 날"이라고 대답합니다. 그의 가슴이 찢어졌을 때, 그의 심장 안에서 라마의 이미지가 발견되었습니다. 라마의 봉사에서 행동할 때 그의 힘은 무한합니다—그는 한번 치유의 약초를 가져오기 위해 산 전체를 들어올렸습니다.

하누만은 힘, 용기, 악으로부터의 보호, 그리고 헌신의 축복을 위해 숭배됩니다. 그는 불멸(치란지비)이며 라마의 이야기가 전해지는 곳마다 헌신의 눈물을 흘리며 듣고 있다고 합니다.""",
    traits_en=["Devoted", "Powerful", "Humble", "Wise", "Protective"],
    traits_ko=["헌신적인", "강력한", "겸손한", "지혜로운", "보호하는"],
    story_en="When Rama's brother Lakshmana lay dying, Hanuman flew to the Himalayas for healing herbs. Unable to identify the right plant, he lifted the entire mountain and brought it to the battlefield, saving Lakshmana's life through his devotion and strength.",
    story_ko="라마의 형제 락슈마나가 죽어가며 누워 있을 때, 하누만은 치유의 약초를 위해 히말라야로 날아갔습니다. 올바른 식물을 식별할 수 없어, 그는 산 전체를 들어올려 전장으로 가져와 그의 헌신과 힘으로 락슈마나의 생명을 구했습니다.",
    match_message_en="Your features carry the devoted strength of Hanuman. There is a humble power to your presence—the look of one whose strength comes from selfless devotion to something greater.",
    match_message_ko="당신의 이목구비는 하누만의 헌신적인 힘을 담고 있습니다. 당신의 존재에는 겸손한 힘이 있습니다—더 큰 것에 대한 이타적 헌신에서 힘이 오는 사람의 모습.",
    image_prompt="Powerful monkey god in devotional pose or flying through sky, muscular form, face of wisdom and devotion, carrying mountain or mace, golden-orange fur, tear of devotion, Rama's image in heart",
    visual_description="Strong simian features, wise devoted eyes, powerful but humble bearing, expression of complete selfless devotion",
    aliases=["Bajrangbali", "Maruti", "हनुमान"],
    era="Hindu Mythology",
    related_characters=["rama", "sita", "lakshmana", "vayu", "ravana"]
)

KRISHNA_DESC = CharacterDescription(
    id="krishna",
    name_en="Krishna",
    name_ko="크리슈나",
    tagline_en="Divine Beloved, Teacher of the Bhagavad Gita",
    tagline_ko="신성한 연인, 바가바드 기타의 스승",
    description_en="""Krishna is the eighth avatar of Vishnu, beloved for his divine childhood pranks, his romantic love with Radha, and his wisdom in the Bhagavad Gita. He embodies divine love in all its forms—from playful affection to the highest spiritual devotion.

As a child, he stole butter and played pranks, charming everyone with his mischief. As a youth, his flute playing enchanted the gopis (cowherd girls), especially Radha, representing the soul's longing for the divine. As an adult, he served as charioteer and guru to Arjuna, teaching the path of dharma.

In the Bhagavad Gita, Krishna reveals the ultimate truth about action, devotion, knowledge, and the nature of self. He is both the accessible, lovable god and the cosmic Supreme Being who contains all universes.""",
    description_ko="""크리슈나는 비슈누의 여덟 번째 아바타로, 신성한 어린 시절의 장난, 라다와의 낭만적 사랑, 바가바드 기타에서의 지혜로 사랑받습니다. 그는 장난스러운 애정에서 가장 높은 영적 헌신까지 모든 형태의 신성한 사랑을 구현합니다.

어린 시절, 그는 버터를 훔치고 장난을 쳐서 모두를 그의 장난으로 매혹시켰습니다. 청년 시절, 그의 플룻 연주가 고피(목동 소녀들), 특히 라다를 매혹시켜 신성에 대한 영혼의 갈망을 대표합니다. 성인으로서, 그는 아르주나의 전차병이자 구루로 봉사하며 다르마의 길을 가르쳤습니다.

바가바드 기타에서, 크리슈나는 행동, 헌신, 지식, 자아의 본성에 대한 궁극적 진실을 드러냅니다. 그는 접근 가능하고 사랑스러운 신이자 모든 우주를 포함하는 우주적 최고 존재입니다.""",
    traits_en=["Playful", "Wise", "Loving", "Divine", "Teaching"],
    traits_ko=["장난스러운", "지혜로운", "사랑하는", "신성한", "가르치는"],
    story_en="On the battlefield of Kurukshetra, Arjuna refused to fight his own family. Krishna revealed his cosmic form, showing that he was the Supreme Being containing all creation, and taught that one must do one's duty without attachment to results—the core message of the Bhagavad Gita.",
    story_ko="쿠룩셰트라 전장에서, 아르주나는 자신의 가족과 싸우기를 거부했습니다. 크리슈나는 그의 우주적 형상을 드러내어 그가 모든 창조를 포함하는 최고 존재임을 보여주고, 결과에 대한 집착 없이 자신의 의무를 해야 한다고 가르쳤습니다—바가바드 기타의 핵심 메시지.",
    match_message_en="Your features carry the divine charm of Krishna. There is a playful yet profound quality to your presence—the look of one who embodies both joy and wisdom.",
    match_message_ko="당신의 이목구비는 크리슈나의 신성한 매력을 담고 있습니다. 당신의 존재에는 장난스러우면서도 깊은 품질이 있습니다—기쁨과 지혜를 모두 구현하는 사람의 모습.",
    image_prompt="Blue-skinned beautiful god playing flute, peacock feather crown, surrounded by cows and gopis in pastoral setting, or as charioteer teaching Arjuna, divine smile, both playful and wise",
    visual_description="Beautiful blue-skinned features, enchanting smile, playful yet wise eyes, expression of divine love and cosmic knowledge",
    aliases=["Govinda", "Keshava", "Madhava", "कृष्ण"],
    era="Hindu Mythology",
    related_characters=["vishnu", "radha", "arjuna", "balarama", "rukmini"]
)

RAMA_DESC = CharacterDescription(
    id="rama",
    name_en="Rama",
    name_ko="라마",
    tagline_en="Ideal King, Embodiment of Dharma",
    tagline_ko="이상적인 왕, 다르마의 구현",
    description_en="""Rama is the seventh avatar of Vishnu, the hero of the Ramayana, and the epitome of dharmic living. He is the ideal son, husband, king, and warrior—maryada purushottam, the perfect man who never strays from righteousness even under the most terrible trials.

Exiled to the forest for fourteen years to honor his father's word, Rama bore hardship without complaint. When his wife Sita was kidnapped by the demon king Ravana, he allied with Hanuman and the monkey army to rescue her, demonstrating that dharma eventually triumphs over evil.

Rama's reign, Rama Rajya, represents the ideal just kingdom. He is worshipped as the embodiment of how a person should live—honoring duty, protecting the innocent, keeping promises, and remaining righteous regardless of personal cost.""",
    description_ko="""라마는 비슈누의 일곱 번째 아바타, 라마야나의 영웅, 다르마적 삶의 전형입니다. 그는 이상적인 아들, 남편, 왕, 전사입니다—마르야다 푸루쇼탐, 가장 끔찍한 시련에서도 결코 의로움에서 벗어나지 않는 완벽한 사람.

아버지의 말을 존중하기 위해 14년간 숲으로 유배되어, 라마는 불평 없이 고난을 견뎠습니다. 그의 아내 시타가 악마 왕 라바나에게 납치되었을 때, 그는 하누만과 원숭이 군대와 동맹하여 그녀를 구출했으며, 다르마가 결국 악을 이긴다는 것을 보여주었습니다.

라마의 통치, 라마 라지야는 이상적인 정의로운 왕국을 대표합니다. 그는 사람이 어떻게 살아야 하는지의 구현으로 숭배됩니다—의무를 존중하고, 무고한 자를 보호하고, 약속을 지키고, 개인적 대가와 관계없이 의롭게 남는 것.""",
    traits_en=["Righteous", "Dutiful", "Ideal", "Devoted", "Just"],
    traits_ko=["의로운", "의무를 다하는", "이상적인", "헌신적인", "공정한"],
    story_en="When Sita was kidnapped, Rama could have used his divine powers to teleport to Lanka. Instead, he walked the long path, building bridges and allying with the vanara, teaching that dharma requires going through proper process, not taking shortcuts even when capable.",
    story_ko="시타가 납치되었을 때, 라마는 신성한 힘을 사용하여 랑카로 순간이동할 수 있었습니다. 대신, 그는 긴 길을 걸으며 다리를 건설하고 바나라와 동맹하여, 능력이 있을 때도 지름길을 택하지 않고 적절한 과정을 거쳐야 한다고 가르쳤습니다.",
    match_message_en="Your features carry the righteous dignity of Rama. There is an ideal quality to your presence—the look of one who never compromises their principles regardless of personal cost.",
    match_message_ko="당신의 이목구비는 라마의 의로운 존엄을 담고 있습니다. 당신의 존재에는 이상적인 품질이 있습니다—개인적 대가와 관계없이 원칙을 타협하지 않는 사람의 모습.",
    image_prompt="Noble prince with bow and arrows, blue skin, in royal or forest setting, Sita at his side, Hanuman devoted nearby, expression of perfect righteousness and gentle strength",
    visual_description="Noble handsome features, calm righteous eyes, royal bearing with gentle strength, expression of perfect dharma",
    aliases=["Ramachandra", "राम"],
    era="Hindu Mythology",
    related_characters=["vishnu", "sita", "hanuman", "lakshmana", "ravana"]
)

PARVATI_DESC = CharacterDescription(
    id="parvati",
    name_en="Parvati",
    name_ko="파르바티",
    tagline_en="Divine Mother, Goddess of Love and Devotion",
    tagline_ko="신성한 어머니, 사랑과 헌신의 여신",
    description_en="""Parvati is the gentle goddess of love, fertility, and devotion—the consort of Shiva and mother of Ganesha and Kartikeya. She is the reincarnation of Sati, Shiva's first wife, who was reborn and performed intense austerities to win Shiva's love again.

As Shakti in her gentle form, Parvati represents the nurturing, life-giving aspect of the divine feminine. She is the balance to Shiva's destructive power, the one who can calm his wildness and bring him back from ascetic withdrawal into engaged life.

Her fierce forms include Durga and Kali, showing that the loving mother can become terrible when her children are threatened. Parvati demonstrates that love itself has the power to transform the universe.""",
    description_ko="""파르바티는 사랑, 다산, 헌신의 온화한 여신—시바의 배우자이자 가네샤와 카르티케야의 어머니입니다. 그녀는 시바의 첫 번째 아내 사티의 환생으로, 다시 태어나 시바의 사랑을 다시 얻기 위해 강렬한 고행을 수행했습니다.

온화한 형태의 샥티로서, 파르바티는 신성한 여성의 양육적이고 생명을 주는 측면을 대표합니다. 그녀는 시바의 파괴적 힘에 대한 균형이며, 그의 거칠음을 진정시키고 금욕적 은둔에서 참여하는 삶으로 데려올 수 있는 존재입니다.

그녀의 맹렬한 형태로는 두르가와 칼리가 있어, 자녀가 위협받을 때 사랑하는 어머니가 끔찍해질 수 있음을 보여줍니다. 파르바티는 사랑 자체가 우주를 변형시키는 힘을 가지고 있음을 보여줍니다.""",
    traits_en=["Loving", "Devoted", "Nurturing", "Determined", "Balancing"],
    traits_ko=["사랑하는", "헌신적인", "양육하는", "결연한", "균형 잡는"],
    story_en="When Shiva was lost in meditation, the gods needed him to marry and have children. They sent Kama, god of love, who was burned to ash by Shiva's third eye. But Parvati's devotion and austerities eventually won Shiva's heart, proving that sincere love conquers even divine resistance.",
    story_ko="시바가 명상에 빠져 있을 때, 신들은 그가 결혼하고 자녀를 가지도록 해야 했습니다. 그들은 사랑의 신 카마를 보냈지만 시바의 세 번째 눈에 의해 재로 타버렸습니다. 그러나 파르바티의 헌신과 고행이 결국 시바의 마음을 얻어, 진심 어린 사랑이 신성한 저항도 정복한다는 것을 증명했습니다.",
    match_message_en="Your features reflect the devoted love of Parvati. There is a nurturing yet determined quality to your presence—the look of one whose gentle love can move mountains.",
    match_message_ko="당신의 이목구비는 파르바티의 헌신적인 사랑을 반영합니다. 당신의 존재에는 양육적이면서도 결연한 품질이 있습니다—온화한 사랑이 산을 움직일 수 있는 사람의 모습.",
    image_prompt="Beautiful Hindu goddess in green and gold, seated with Shiva or holding their children, gentle maternal expression, lotus and divine light, Mount Kailash home, loving peaceful presence",
    visual_description="Beautiful gentle features, loving maternal eyes, graceful form, expression of devoted love and nurturing strength",
    aliases=["Uma", "Gauri", "पार्वती"],
    era="Hindu Mythology",
    related_characters=["shiva", "ganesha", "kartikeya", "durga", "kali"]
)


INDRA_DESC = CharacterDescription(
    id="indra",
    name_en="Indra",
    name_ko="인드라",
    tagline_en="King of Gods, Lord of Storms and War",
    tagline_ko="신들의 왕, 폭풍과 전쟁의 주인",
    description_en="""Indra is the king of the Devas and ruler of Svarga (heaven). He wields the thunderbolt Vajra and rides the white elephant Airavata. As god of storms, rain, and war, he is the mightiest of the Vedic gods.

His greatest feat was slaying the serpent Vritra who had imprisoned all the world's waters, releasing them to flow as rivers and bring life to the land. Indra represents the cosmic battle between order and chaos, light and darkness.

Though his prominence decreased in later Hinduism, Indra remains the archetypal divine warrior—powerful, glorious, but also flawed and subject to karma like all beings.""",
    description_ko="""인드라는 데바들의 왕이자 스바르가(천국)의 통치자입니다. 그는 번개 바즈라를 휘두르고 흰 코끼리 아이라바타를 탑니다. 폭풍, 비, 전쟁의 신으로서, 그는 베다 신들 중 가장 강력합니다.

그의 가장 큰 업적은 세상의 모든 물을 가두었던 뱀 브리트라를 죽여 물이 강으로 흘러 땅에 생명을 가져오게 한 것입니다. 인드라는 질서와 혼돈, 빛과 어둠 사이의 우주적 전투를 대표합니다.

후대 힌두교에서 그의 중요성은 감소했지만, 인드라는 원형적인 신성한 전사로 남아 있습니다—강력하고, 영광스럽지만, 또한 결함이 있고 모든 존재처럼 카르마에 종속됩니다.""",
    traits_en=["Powerful", "Warrior", "Stormy", "Glorious", "Flawed"],
    traits_ko=["강력한", "전사", "폭풍우의", "영광스러운", "결함 있는"],
    story_en="The serpent Vritra had swallowed all the world's waters, causing terrible drought. Indra, fortified by soma, took up his vajra and battled the demon. With a mighty blow he split Vritra open, releasing the waters that became the rivers of the world.",
    story_ko="뱀 브리트라가 세상의 모든 물을 삼켜 끔찍한 가뭄을 일으켰습니다. 소마로 강화된 인드라는 바즈라를 들고 악마와 싸웠습니다. 강력한 일격으로 그는 브리트라를 갈라 세상의 강이 된 물들을 풀어주었습니다.",
    match_message_en="Your features carry the stormy power of Indra. There is warrior kingship in your appearance—the look of one who fights cosmic battles and commands the forces of nature.",
    match_message_ko="당신의 이목구비는 인드라의 폭풍우 같은 힘을 담고 있습니다. 당신의 외모에는 전사 왕다움이 있습니다—우주적 전투를 치르고 자연의 힘을 지휘하는 사람의 모습.",
    image_prompt="Powerful Hindu god on white elephant wielding thunderbolt vajra, storm clouds and lightning behind, golden armor and crown, heroic warrior expression, Vedic divine style",
    visual_description="Powerful regal features, fierce stormy eyes, commanding warrior presence, expression of divine king ready for battle",
    aliases=["Shakra", "Lord of Svarga", "इन्द्र"],
    era="Hindu Mythology",
    related_characters=["vritra", "agni", "varuna", "soma"]
)

AGNI_DESC = CharacterDescription(
    id="agni",
    name_en="Agni",
    name_ko="아그니",
    tagline_en="God of Fire, Divine Messenger",
    tagline_ko="불의 신, 신성한 메신저",
    description_en="""Agni is the god of fire in all its forms—the sacrificial fire, the household hearth, the fire of digestion, and the fire of the sun. As the medium of sacrifice, he carries offerings from humans to the gods, making him the essential bridge between worlds.

With two faces—one benevolent and one fierce—Agni embodies fire's dual nature: life-giving warmth and destructive conflagration. He is present at every Hindu ritual, purifying offerings and carrying prayers to heaven.

Agni represents transformation through fire, the purifying power that changes matter to energy, and the sacred connection between the mortal and divine realms.""",
    description_ko="""아그니는 모든 형태의 불의 신입니다—제사의 불, 가정의 화덕, 소화의 불, 태양의 불. 제사의 매개체로서, 그는 인간의 제물을 신들에게 전달하여 세계 사이의 필수적인 다리가 됩니다.

두 얼굴—하나는 자비롭고 하나는 사나운—을 가진 아그니는 불의 이중적 본성을 구현합니다: 생명을 주는 온기와 파괴적인 화염. 그는 모든 힌두 의식에 존재하여 제물을 정화하고 기도를 천국으로 전달합니다.

아그니는 불을 통한 변환, 물질을 에너지로 바꾸는 정화의 힘, 그리고 필멸자와 신성한 영역 사이의 신성한 연결을 대표합니다.""",
    traits_en=["Transforming", "Purifying", "Messenger", "Dual-natured", "Sacred"],
    traits_ko=["변환하는", "정화하는", "메신저", "이중적 본성의", "신성한"],
    story_en="When the gods needed to communicate with humans, they chose Agni as their messenger. Every sacrifice placed in fire reaches the gods through Agni's flames. His tongue of fire licks the offerings, transforming them into divine nourishment.",
    story_ko="신들이 인간과 소통해야 했을 때, 그들은 아그니를 메신저로 선택했습니다. 불에 놓인 모든 제물은 아그니의 불꽃을 통해 신들에게 도달합니다. 그의 불의 혀가 제물을 핥아 신성한 양분으로 변환합니다.",
    match_message_en="Your features carry the transforming power of Agni. There is sacred fire in your appearance—the look of one who purifies and transforms, bridging the gap between the earthly and divine.",
    match_message_ko="당신의 이목구비는 아그니의 변환하는 힘을 담고 있습니다. 당신의 외모에는 신성한 불이 있습니다—정화하고 변환하며, 지상과 신성 사이의 간격을 연결하는 사람의 모습.",
    image_prompt="Two-faced Hindu fire god with flames as hair and beard, riding ram, carrying offerings upward in smoke, sacred fire colors of red orange and gold, divine transformative presence",
    visual_description="Radiant fiery features, blazing intense eyes, dual expression showing both gentle and fierce, appearance of living flame",
    aliases=["The Fire God", "Divine Messenger", "अग्नि"],
    era="Hindu Mythology",
    related_characters=["indra", "soma", "vayu", "brahma"]
)

KARTIKEYA_DESC = CharacterDescription(
    id="kartikeya",
    name_en="Kartikeya",
    name_ko="카르티케야",
    tagline_en="God of War, Commander of Divine Armies",
    tagline_ko="전쟁의 신, 신성한 군대의 사령관",
    description_en="""Kartikeya is the god of war and the commander of the armies of the gods. Son of Shiva and Parvati, he was born to defeat the demon Tarakasura whom no one else could kill. He rides the peacock Paravani and wields the divine spear Vel.

With six heads and twelve arms, Kartikeya sees in all directions at once and can engage multiple enemies simultaneously. He represents the focused power of divine will directed toward righteous victory.

Kartikeya embodies martial valor in service of dharma, the discipline and focus of the spiritual warrior, and the truth that sometimes evil must be confronted directly with force.""",
    description_ko="""카르티케야는 전쟁의 신이자 신들의 군대 사령관입니다. 시바와 파르바티의 아들로, 다른 누구도 죽일 수 없는 악마 타라카수라를 물리치기 위해 태어났습니다. 그는 공작새 파라바니를 타고 신성한 창 벨을 휘두릅니다.

여섯 머리와 열두 팔을 가진 카르티케야는 모든 방향을 한 번에 보고 동시에 여러 적과 교전할 수 있습니다. 그는 정당한 승리를 향해 집중된 신성한 의지의 힘을 대표합니다.

카르티케야는 다르마를 위한 전투적 용맹, 영적 전사의 규율과 집중, 그리고 때로는 악을 힘으로 직접 대면해야 한다는 진실을 구현합니다.""",
    traits_en=["Warrior", "Commanding", "Youthful", "Focused", "Victorious"],
    traits_ko=["전사", "지휘하는", "젊은", "집중된", "승리하는"],
    story_en="The demon Tarakasura had a boon that only a son of Shiva could kill him—and Shiva was an ascetic who would never marry. Yet through divine intervention, Kartikeya was born and led the gods to battle. With his divine spear, he slew Tarakasura and restored cosmic order.",
    story_ko="악마 타라카수라는 시바의 아들만이 그를 죽일 수 있다는 축복을 받았습니다—그리고 시바는 결코 결혼하지 않을 고행자였습니다. 그러나 신성한 개입을 통해 카르티케야가 태어났고 신들을 전투로 이끌었습니다. 그의 신성한 창으로 타라카수라를 죽이고 우주의 질서를 회복했습니다.",
    match_message_en="Your features carry the martial focus of Kartikeya. There is commander's presence in your appearance—the look of one who leads divine battles and strikes with precision and purpose.",
    match_message_ko="당신의 이목구비는 카르티케야의 전투적 집중을 담고 있습니다. 당신의 외모에는 사령관의 존재감이 있습니다—신성한 전투를 이끌고 정확함과 목적을 가지고 타격하는 사람의 모습.",
    image_prompt="Youthful Hindu war god with six heads riding peacock, wielding divine spear Vel, army of gods behind, victorious battle stance, radiant martial divine energy",
    visual_description="Youthful fierce features, multiple focused gazes, commanding military bearing, expression of righteous martial focus",
    aliases=["Murugan", "Skanda", "कार्तिकेय"],
    era="Hindu Mythology",
    related_characters=["shiva", "parvati", "ganesha", "indra"]
)

RADHA_DESC = CharacterDescription(
    id="radha",
    name_en="Radha",
    name_ko="라다",
    tagline_en="Supreme Goddess of Love, Eternal Beloved",
    tagline_ko="사랑의 최고 여신, 영원한 연인",
    description_en="""Radha is the eternal consort and supreme beloved of Krishna, embodying the perfection of divine love. Her love for Krishna represents the soul's longing for union with the divine, the highest form of devotion that transcends all worldly attachments.

In Vaishnavism, Radha is considered the supreme goddess, the feminine aspect of the divine whose love draws Krishna himself. Their eternal love-play in the forests of Vrindavan is the cosmic drama of separation and union that defines existence.

Radha represents the power of devotional love, the feminine divine that completes and draws the masculine, and the truth that the path to the divine is through the heart.""",
    description_ko="""라다는 크리슈나의 영원한 배우자이자 최고의 연인으로, 신성한 사랑의 완벽함을 구현합니다. 크리슈나에 대한 그녀의 사랑은 신과의 합일을 갈망하는 영혼, 모든 세속적 집착을 초월하는 최고의 헌신을 대표합니다.

바이슈나비즘에서 라다는 최고의 여신으로 여겨지며, 크리슈나 자신을 끌어당기는 신성한 여성적 측면입니다. 브린다반 숲에서의 그들의 영원한 사랑의 유희는 존재를 정의하는 분리와 합일의 우주적 드라마입니다.

라다는 헌신적 사랑의 힘, 남성을 완성하고 끌어당기는 여성적 신성, 그리고 신에게 이르는 길은 마음을 통해서라는 진실을 대표합니다.""",
    traits_en=["Devoted", "Loving", "Supreme", "Longing", "Blissful"],
    traits_ko=["헌신적인", "사랑하는", "최고의", "그리워하는", "지복의"],
    story_en="In the forests of Vrindavan, Radha and Krishna would meet in secret, their love transcending all social bounds. When Krishna left for Mathura, Radha's separation became the model of divine longing—the pain of the soul separated from its beloved that drives spiritual seeking.",
    story_ko="브린다반의 숲에서 라다와 크리슈나는 비밀리에 만났고, 그들의 사랑은 모든 사회적 경계를 초월했습니다. 크리슈나가 마투라로 떠났을 때, 라다의 분리는 신성한 그리움의 모델이 되었습니다—영적 추구를 이끄는 사랑하는 이와 분리된 영혼의 고통.""",
    match_message_en="Your features carry the divine devotion of Radha. There is pure love in your appearance—the look of one whose heart is given completely to the beloved, embodying the highest devotion.",
    match_message_ko="당신의 이목구비는 라다의 신성한 헌신을 담고 있습니다. 당신의 외모에는 순수한 사랑이 있습니다—마음을 연인에게 완전히 바치고 최고의 헌신을 구현하는 사람의 모습.",
    image_prompt="Beautiful Hindu goddess in devotional pose with Krishna, lotus flowers and peacock feathers, Vrindavan forest setting, expression of divine love and longing, golden radiant devotional style",
    visual_description="Beautiful devoted features, eyes full of divine love and longing, graceful loving presence, expression of complete devotional surrender",
    aliases=["Radhika", "Radharani", "राधा"],
    era="Hindu Mythology",
    related_characters=["krishna", "lakshmi", "vishnu", "gopis"]
)

YAMA_DESC = CharacterDescription(
    id="yama",
    name_en="Yama",
    name_ko="야마",
    tagline_en="God of Death and Justice",
    tagline_ko="죽음과 정의의 신",
    description_en="""Yama is the god of death and the first mortal who died, becoming the ruler of the dead. He judges the souls of the deceased based on their karma, determining their fate in the cycle of rebirth. He rides a black buffalo and carries a noose to bind souls.

As Dharmaraja, the King of Dharma, Yama is utterly impartial—no bribe or plea can sway his judgment. He consults the records kept by Chitragupta to determine each soul's accumulated karma and pronounce their destination.

Yama represents the inescapability of death, the just accounting of all deeds, and the truth that our actions determine our fate beyond this life.""",
    description_ko="""야마는 죽음의 신이자 최초로 죽은 필멸자로, 죽은 자들의 통치자가 되었습니다. 그는 고인의 영혼을 카르마에 따라 심판하여 환생의 순환에서 그들의 운명을 결정합니다. 그는 검은 물소를 타고 영혼을 묶을 올가미를 들고 다닙니다.

다르마라자, 다르마의 왕으로서, 야마는 완전히 공정합니다—어떤 뇌물이나 간청도 그의 판결을 흔들 수 없습니다. 그는 치트라굽타가 기록한 기록을 참조하여 각 영혼의 축적된 카르마를 결정하고 그들의 목적지를 선언합니다.

야마는 죽음의 불가피함, 모든 행위의 공정한 회계, 그리고 우리의 행동이 이 삶 너머의 운명을 결정한다는 진실을 대표합니다.""",
    traits_en=["Just", "Impartial", "Inevitable", "Judging", "Truthful"],
    traits_ko=["공정한", "공평한", "불가피한", "심판하는", "진실한"],
    story_en="When Savitri's husband Satyavan died, she followed Yama to the realm of death. So impressed was Yama by her devotion that he offered her any boon except her husband's life. Savitri cleverly asked for sons—which required Satyavan alive—and Yama honored his word.",
    story_ko="사비트리의 남편 사티아반이 죽었을 때, 그녀는 야마를 따라 죽음의 영역으로 갔습니다. 야마는 그녀의 헌신에 너무 감동하여 남편의 생명을 제외한 어떤 축복이든 주겠다고 했습니다. 사비트리는 영리하게 아들들을 요청했고—이것은 사티아반이 살아있어야 했습니다—야마는 자신의 말을 지켰습니다.",
    match_message_en="Your features carry the just severity of Yama. There is impartial truth in your appearance—the look of one who sees all deeds clearly and judges without favor or malice.",
    match_message_ko="당신의 이목구비는 야마의 공정한 엄격함을 담고 있습니다. 당신의 외모에는 공평한 진실이 있습니다—모든 행위를 명확히 보고 호의나 악의 없이 심판하는 사람의 모습.",
    image_prompt="Dark-skinned Hindu god riding black buffalo, holding noose and mace, scales of justice, souls awaiting judgment, expression of impartial divine justice, solemn underworld setting",
    visual_description="Severe dignified features, all-seeing judgmental eyes, dark commanding presence, expression of impartial cosmic justice",
    aliases=["Dharmaraja", "Lord of Death", "यम"],
    era="Hindu Mythology",
    related_characters=["chitragupta", "savitri", "nachiketa"]
)

SURYA_DESC = CharacterDescription(
    id="surya",
    name_en="Surya",
    name_ko="수리야",
    tagline_en="God of the Sun, Source of Life",
    tagline_ko="태양의 신, 생명의 원천",
    description_en="""Surya is the god of the sun, riding his chariot drawn by seven horses across the sky each day. He is the visible form of the divine, the source of light, warmth, and life. His rays dispel darkness both literal and spiritual.

Father of Karna and the divine twins the Ashvins, Surya represents the life-giving power that makes all existence possible. The ancient Gayatri Mantra is addressed to Surya's light, seeking enlightenment and wisdom.

Surya represents the divine light of consciousness, the truth that dispels ignorance, and the eternal cycle of day that governs all life.""",
    description_ko="""수리야는 태양의 신으로, 매일 일곱 마리 말이 끄는 전차를 타고 하늘을 가로지릅니다. 그는 신성의 가시적 형태이자, 빛, 온기, 생명의 원천입니다. 그의 광선은 문자 그대로의 어둠과 영적인 어둠 모두를 물리칩니다.

카르나와 신성한 쌍둥이 아쉬빈의 아버지인 수리야는 모든 존재를 가능하게 하는 생명을 주는 힘을 대표합니다. 고대 가야트리 만트라는 수리야의 빛에 바쳐져 깨달음과 지혜를 구합니다.

수리야는 의식의 신성한 빛, 무지를 물리치는 진실, 그리고 모든 생명을 지배하는 낮의 영원한 순환을 대표합니다.""",
    traits_en=["Radiant", "Life-giving", "Witnessing", "Enlightening", "Eternal"],
    traits_ko=["빛나는", "생명을 주는", "목격하는", "깨달음을 주는", "영원한"],
    story_en="Surya's brilliance was so intense that his wife Sanjna fled from him. To win her back, his father-in-law Vishwakarma reduced Surya's radiance, using the excess light to forge divine weapons including Vishnu's discus and Shiva's trident.",
    story_ko="수리야의 광채가 너무 강렬해서 그의 아내 산즈나가 그에게서 도망쳤습니다. 그녀를 되찾기 위해 그의 장인 비슈바카르마가 수리야의 광채를 줄였고, 남은 빛으로 비슈누의 원반과 시바의 삼지창을 포함한 신성한 무기를 만들었습니다.",
    match_message_en="Your features carry the radiant power of Surya. There is illuminating presence in your appearance—the look of one who brings light to all they see and dispels darkness wherever they go.",
    match_message_ko="당신의 이목구비는 수리야의 빛나는 힘을 담고 있습니다. 당신의 외모에는 빛나는 존재감이 있습니다—보는 모든 것에 빛을 가져다주고 가는 곳마다 어둠을 물리치는 사람의 모습.",
    image_prompt="Radiant Hindu sun god in golden chariot pulled by seven horses across sky, blazing corona of light, hands raised in blessing, expression of divine illumination, celestial golden atmosphere",
    visual_description="Radiant golden features, brilliant all-seeing eyes, blazing luminous presence, expression of enlightening divine power",
    aliases=["Aditya", "The Sun God", "सूर्य"],
    era="Hindu Mythology",
    related_characters=["karna", "ashvins", "sanjna", "yama"]
)

VARUNA_DESC = CharacterDescription(
    id="varuna",
    name_en="Varuna",
    name_ko="바루나",
    tagline_en="God of Oceans and Cosmic Order",
    tagline_ko="바다와 우주 질서의 신",
    description_en="""Varuna is the god of the oceans, water, and the celestial ocean of the night sky. In the Vedas, he was one of the most important gods, the keeper of cosmic order (Rita) who enforced divine law and punished wrongdoers.

He sees all that happens and knows all secrets—his thousand eyes are the stars that watch from heaven. Those who break oaths or violate dharma fear Varuna's noose, which binds sinners.

Varuna represents the encompassing cosmic order, the moral law that underlies existence, and the divine surveillance that sees all deeds and thoughts.""",
    description_ko="""바루나는 바다, 물, 그리고 밤하늘의 천상의 바다의 신입니다. 베다에서 그는 가장 중요한 신 중 하나였으며, 우주 질서(리타)의 수호자로서 신성한 법을 집행하고 악인을 벌했습니다.

그는 일어나는 모든 것을 보고 모든 비밀을 압니다—그의 천 개의 눈은 하늘에서 지켜보는 별들입니다. 맹세를 어기거나 다르마를 위반하는 자들은 죄인을 묶는 바루나의 올가미를 두려워합니다.

바루나는 포괄하는 우주 질서, 존재의 기초가 되는 도덕법, 그리고 모든 행위와 생각을 보는 신성한 감시를 대표합니다.""",
    traits_en=["Cosmic", "Oceanic", "All-seeing", "Law-keeping", "Ancient"],
    traits_ko=["우주적인", "바다의", "모든 것을 보는", "법을 지키는", "고대의"],
    story_en="When the sage Vasishtha was falsely accused, Varuna appeared as witness, for nothing escapes his sight. He declared the sage innocent, for Varuna sees truth even when it is hidden from all others. His justice restored the sage's honor.",
    story_ko="현자 바시슈타가 거짓으로 고발당했을 때, 바루나가 증인으로 나타났습니다. 왜냐하면 그의 시야를 피하는 것은 없기 때문입니다. 그는 현자를 무죄로 선언했습니다. 바루나는 다른 모든 이에게 숨겨졌을 때도 진실을 보기 때문입니다. 그의 정의가 현자의 명예를 회복시켰습니다.",
    match_message_en="Your features carry the cosmic depth of Varuna. There is oceanic wisdom in your appearance—the look of one who sees all secrets and upholds the moral order of existence.",
    match_message_ko="당신의 이목구비는 바루나의 우주적 깊이를 담고 있습니다. 당신의 외모에는 바다같은 지혜가 있습니다—모든 비밀을 보고 존재의 도덕적 질서를 유지하는 사람의 모습.",
    image_prompt="Ancient Hindu ocean god riding mythical sea creature, holding noose and pot of water, ocean waves and starry sky merging, thousand eyes as stars, expression of cosmic law-keeping",
    visual_description="Deep ancient features, thousand-eyed cosmic gaze, oceanic fluid presence, expression of one who keeps cosmic law",
    aliases=["Lord of Waters", "Keeper of Rita", "वरुण"],
    era="Hindu Mythology",
    related_characters=["indra", "mitra", "agni"]
)

ARJUNA_DESC = CharacterDescription(
    id="arjuna",
    name_en="Arjuna",
    name_ko="아르주나",
    tagline_en="Greatest Warrior, Seeker of Dharma",
    tagline_ko="가장 위대한 전사, 다르마의 탐구자",
    description_en="""Arjuna is the hero of the Mahabharata, the greatest archer of his age and the chosen recipient of Krishna's teachings in the Bhagavad Gita. Facing his kinsmen in battle, Arjuna's moral crisis led to the most profound philosophical dialogue in Hindu scripture.

His bow Gandiva never missed its mark, and he was trained by the gods themselves. Yet it was his crisis of conscience—his refusal to fight his own family—that made him the vehicle for eternal wisdom.

Arjuna represents the spiritual seeker facing life's hardest questions, the warrior who must find right action amidst moral complexity, and the devotee who surrenders to divine guidance.""",
    description_ko="""아르주나는 마하바라타의 영웅이자 그의 시대 가장 위대한 궁수이며 바가바드 기타에서 크리슈나의 가르침을 받은 선택된 수혜자입니다. 전투에서 친족을 마주한 아르주나의 도덕적 위기는 힌두 경전에서 가장 심오한 철학적 대화로 이어졌습니다.

그의 활 간디바는 목표를 놓친 적이 없었고, 그는 신들에게 직접 훈련받았습니다. 그러나 그를 영원한 지혜의 도구로 만든 것은 그의 양심의 위기—자신의 가족과 싸우기를 거부한 것—이었습니다.

아르주나는 삶의 가장 어려운 질문에 직면한 영적 탐구자, 도덕적 복잡성 속에서 올바른 행동을 찾아야 하는 전사, 그리고 신의 인도에 항복하는 헌신자를 대표합니다.""",
    traits_en=["Skilled", "Questioning", "Devoted", "Conflicted", "Heroic"],
    traits_ko=["숙련된", "질문하는", "헌신적인", "갈등하는", "영웅적인"],
    story_en="Before the great battle, Arjuna saw his teachers, uncles, and cousins arrayed against him. He dropped his bow, unable to fight. Krishna then taught him the Bhagavad Gita—the path of duty, devotion, and knowledge that resolves all moral conflict.",
    story_ko="대전투 전, 아르주나는 자신의 스승들, 삼촌들, 사촌들이 자신에게 대항하여 배열된 것을 보았습니다. 그는 활을 떨어뜨리고 싸울 수 없었습니다. 그때 크리슈나는 그에게 바가바드 기타—모든 도덕적 갈등을 해결하는 의무, 헌신, 지식의 길을 가르쳤습니다.",
    match_message_en="Your features carry the questioning heroism of Arjuna. There is noble seeking in your appearance—the look of one who faces hard truths and finds wisdom through surrender to higher guidance.",
    match_message_ko="당신의 이목구비는 아르주나의 질문하는 영웅심을 담고 있습니다. 당신의 외모에는 고귀한 탐구가 있습니다—어려운 진실에 직면하고 더 높은 인도에 대한 항복을 통해 지혜를 찾는 사람의 모습.",
    image_prompt="Noble Indian warrior prince with divine bow Gandiva, Krishna as charioteer behind, battlefield of Kurukshetra, expression of moral questioning transforming to determination, epic Hindu style",
    visual_description="Noble heroic features, eyes showing both doubt and devotion, warrior bearing with spiritual depth, expression of one who questions and then acts",
    aliases=["Partha", "The Mighty Armed", "अर्जुन"],
    era="Hindu Mythology",
    related_characters=["krishna", "draupadi", "yudhishthira", "bhima"]
)


# Dictionary of Hindu descriptions
HINDU_DESCRIPTIONS = {
    "shiva": SHIVA_DESC,
    "vishnu": VISHNU_DESC,
    "brahma": BRAHMA_DESC,
    "ganesha": GANESHA_DESC,
    "lakshmi": LAKSHMI_DESC,
    "saraswati": SARASWATI_DESC,
    "kali": KALI_DESC,
    "durga": DURGA_DESC,
    "hanuman": HANUMAN_DESC,
    "krishna": KRISHNA_DESC,
    "rama": RAMA_DESC,
    "parvati": PARVATI_DESC,
    "indra": INDRA_DESC,
    "agni": AGNI_DESC,
    "kartikeya": KARTIKEYA_DESC,
    "radha": RADHA_DESC,
    "yama": YAMA_DESC,
    "surya": SURYA_DESC,
    "varuna": VARUNA_DESC,
    "arjuna": ARJUNA_DESC,
}
