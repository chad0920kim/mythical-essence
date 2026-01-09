"""
Christian Saints and Figures Character Descriptions
Contains detailed descriptions for major Christian saints and religious figures
"""
from .descriptions import CharacterDescription


VIRGIN_MARY_DESC = CharacterDescription(
    id="virgin_mary",
    name_en="Virgin Mary",
    name_ko="성모 마리아",
    tagline_en="Mother of God, Queen of Heaven",
    tagline_ko="하느님의 어머니, 천상의 모후",
    description_en="""The Virgin Mary, also known as the Blessed Virgin or Our Lady, is the mother of Jesus Christ in Christian tradition. She is venerated as the greatest of all saints and holds a unique position in Christianity as Theotokos—the God-bearer.

According to the Gospels, Mary was a young Jewish woman from Nazareth chosen by God to bear His son. Through the Annunciation, the angel Gabriel informed her of her divine role, and she accepted with the words "Let it be done unto me according to your word."

Mary represents perfect faith, humility, and maternal love. She stood at the foot of the cross during her son's crucifixion and was present with the apostles at Pentecost. Throughout Christian history, countless believers have turned to her as intercessor and mother of all Christians.""",
    description_ko="""복되신 동정녀 또는 우리 어머니로도 알려진 성모 마리아는 기독교 전통에서 예수 그리스도의 어머니입니다. 그녀는 모든 성인 중 가장 위대한 분으로 공경받으며, 테오토코스—하느님을 품은 분—로서 기독교에서 독특한 위치를 차지합니다.

복음서에 따르면, 마리아는 나자렛의 젊은 유대인 여성으로 하느님께서 그의 아들을 낳도록 선택하셨습니다. 수태고지를 통해 천사 가브리엘이 그녀에게 신성한 역할을 알렸고, 그녀는 "말씀대로 저에게 이루어지소서"라는 말로 받아들였습니다.

마리아는 완벽한 믿음, 겸손, 모성애를 상징합니다. 그녀는 아들의 십자가형 때 십자가 아래에 섰고, 성령 강림절에 사도들과 함께 있었습니다. 기독교 역사를 통틀어, 수많은 신자들이 중보자이자 모든 그리스도인의 어머니로서 그녀에게 의지해왔습니다.""",
    traits_en=["Holy", "Humble", "Maternal", "Faithful", "Intercessory"],
    traits_ko=["거룩한", "겸손한", "모성적인", "신실한", "중보하는"],
    story_en="When the wine ran out at the wedding at Cana, Mary approached Jesus saying 'They have no wine.' Though His hour had not yet come, Jesus performed His first miracle at His mother's request, turning water into the finest wine.",
    story_ko="가나의 혼인잔치에서 포도주가 떨어졌을 때, 마리아는 예수님께 다가가 '그들에게 포도주가 없다'고 말했습니다. 아직 그의 때가 오지 않았지만, 예수님은 어머니의 청에 첫 번째 기적을 행하시어 물을 최상의 포도주로 바꾸셨습니다.",
    match_message_en="You radiate the holy grace of Mary. There is a humble, maternal quality to your presence—the look of one whose faith and love are perfect and unwavering.",
    match_message_ko="당신은 마리아의 거룩한 은총을 발산합니다. 당신의 존재에는 겸손하고 모성적인 품질이 있습니다—믿음과 사랑이 완벽하고 변함없는 사람의 모습.",
    image_prompt="Serene holy woman in blue mantle over white robes, gentle maternal expression, golden halo, hands in prayer, surrounded by roses and lilies",
    visual_description="Gentle serene features, compassionate loving eyes, humble graceful bearing, expression of perfect maternal love and faith",
    aliases=["Blessed Virgin Mary", "Our Lady", "Madonna", "Theotokos"],
    era="Biblical (1st century)",
    related_characters=["jesus", "saint_joseph", "saint_gabriel"]
)

SAINT_MICHAEL_DESC = CharacterDescription(
    id="saint_michael",
    name_en="Saint Michael",
    name_ko="대천사 미카엘",
    tagline_en="Archangel and Warrior of God",
    tagline_ko="대천사이자 하느님의 전사",
    description_en="""Saint Michael the Archangel is the greatest of all angels in Christian tradition, the commander of God's heavenly armies and the champion of justice. His name means "Who is like God?"—a battle cry against all that opposes the divine.

In the Book of Revelation, Michael leads the hosts of heaven against Satan and his fallen angels, casting them down from paradise. He is the protector of the faithful, the guardian of the Church, and the one who weighs souls on Judgment Day.

Michael represents divine justice, courage, and the ultimate victory of good over evil. He is depicted as a warrior angel in armor, often with his foot upon the defeated dragon, sword or spear in hand. Soldiers, police, and all who protect others have long claimed him as their patron.""",
    description_ko="""대천사 성 미카엘은 기독교 전통에서 모든 천사 중 가장 위대하며, 하느님의 천상 군대의 사령관이자 정의의 챔피언입니다. 그의 이름은 "누가 하느님과 같으랴?"라는 뜻으로—신성에 반대하는 모든 것에 대한 전투 함성입니다.

요한묵시록에서, 미카엘은 천상의 무리를 이끌고 사탄과 그의 타락한 천사들에 맞서 싸워, 그들을 낙원에서 쫓아냅니다. 그는 신자들의 보호자, 교회의 수호자, 심판의 날에 영혼을 저울질하는 자입니다.

미카엘은 신성한 정의, 용기, 선이 악에 대한 궁극적인 승리를 상징합니다. 그는 갑옷을 입은 전사 천사로 묘사되며, 종종 패배한 용을 발 아래 두고 검이나 창을 손에 들고 있습니다. 군인, 경찰, 그리고 타인을 보호하는 모든 사람들이 오랫동안 그를 그들의 수호성인으로 삼아왔습니다.""",
    traits_en=["Warrior", "Just", "Protective", "Victorious", "Divine"],
    traits_ko=["전사적인", "공정한", "수호하는", "승리하는", "신성한"],
    story_en="When Lucifer rebelled against God, it was Michael who stepped forward to lead heaven's faithful angels. With the cry 'Who is like God?' he cast down the proud rebel and all who followed him, establishing the eternal victory of good over evil.",
    story_ko="루시퍼가 하느님께 반역했을 때, 천상의 충실한 천사들을 이끌기 위해 나선 것은 미카엘이었습니다. '누가 하느님과 같으랴!'라는 외침과 함께 그는 교만한 반역자와 그를 따르는 모든 자들을 쫓아내어, 선이 악을 이기는 영원한 승리를 확립했습니다.",
    match_message_en="You carry the righteous strength of Michael. There is a protective, warrior's quality to your presence—the look of one who stands against evil and defends the innocent.",
    match_message_ko="당신은 미카엘의 의로운 힘을 지니고 있습니다. 당신의 존재에는 수호하고 전사적인 품질이 있습니다—악에 맞서고 무고한 자를 지키는 사람의 모습.",
    image_prompt="Powerful warrior angel in golden armor with massive wings, holding flaming sword, standing victorious over defeated dragon, divine light radiating",
    visual_description="Strong noble features, fierce righteous eyes, powerful warrior bearing, expression of divine justice and protective strength",
    aliases=["Archangel Michael", "Saint Michel", "Chief of Angels"],
    era="Biblical/Eternal",
    related_characters=["saint_gabriel", "saint_raphael", "lucifer"]
)

SAINT_GABRIEL_DESC = CharacterDescription(
    id="saint_gabriel",
    name_en="Saint Gabriel",
    name_ko="대천사 가브리엘",
    tagline_en="Messenger Angel, Herald of Divine News",
    tagline_ko="전령 천사, 하느님 소식의 선포자",
    description_en="""Saint Gabriel the Archangel is God's chief messenger, the bearer of the most important divine announcements in biblical history. His name means "God is my strength," and he appears at pivotal moments to deliver news that changes the course of salvation.

Gabriel announced to the prophet Daniel the coming of the Messiah, to Zechariah the birth of John the Baptist, and most famously to Mary that she would bear the Son of God. Each apparition brought transformative news that shaped human destiny.

Gabriel represents divine communication, revelation, and the moment when heaven touches earth with world-changing news. He is often depicted holding a lily, symbolizing purity, or a trumpet to announce God's messages. He is the patron of communications workers and diplomats.""",
    description_ko="""대천사 성 가브리엘은 하느님의 수석 전령으로, 성경 역사에서 가장 중요한 신성한 발표들을 전하는 자입니다. 그의 이름은 "하느님이 나의 힘이시다"라는 뜻이며, 구원의 과정을 바꾸는 소식을 전하기 위해 중요한 순간에 나타납니다.

가브리엘은 예언자 다니엘에게 메시아의 오심을, 즈카르야에게 세례자 요한의 탄생을, 그리고 가장 유명하게 마리아에게 하느님의 아들을 낳을 것임을 알렸습니다. 각 발현은 인류의 운명을 형성하는 변혁적인 소식을 가져왔습니다.

가브리엘은 신성한 소통, 계시, 천상이 세상을 바꾸는 소식으로 땅에 닿는 순간을 상징합니다. 그는 종종 순결을 상징하는 백합을 들고 있거나, 하느님의 메시지를 알리는 나팔을 들고 있는 모습으로 묘사됩니다. 그는 통신 종사자와 외교관의 수호성인입니다.""",
    traits_en=["Messenger", "Revelatory", "Pure", "Momentous", "Divine"],
    traits_ko=["전령의", "계시하는", "순수한", "중대한", "신성한"],
    story_en="When Gabriel appeared to Mary in Nazareth, he greeted her with 'Hail, full of grace, the Lord is with you.' With these words began the most important announcement in history—that the Virgin would conceive and bear Emmanuel, God-with-us.",
    story_ko="가브리엘이 나자렛에서 마리아에게 나타났을 때, 그는 '은총이 가득한 이여, 기뻐하여라. 주님께서 너와 함께 계시다'라고 인사했습니다. 이 말로 역사상 가장 중요한 발표가 시작되었습니다—동정녀가 잉태하여 임마누엘, 하느님께서 우리와 함께 계심을 낳을 것이라는 것.",
    match_message_en="You carry the messenger spirit of Gabriel. There is a pure, revelatory quality to your presence—the look of one who brings important news and speaks truth.",
    match_message_ko="당신은 가브리엘의 전령 정신을 지니고 있습니다. 당신의 존재에는 순수하고 계시적인 품질이 있습니다—중요한 소식을 전하고 진실을 말하는 사람의 모습.",
    image_prompt="Graceful angel with gentle features holding white lily, soft wings, messenger's bearing, golden light, scene of divine announcement",
    visual_description="Gentle refined features, calm knowing eyes, graceful messenger's bearing, expression of divine communication and purity",
    aliases=["Archangel Gabriel", "Angel of the Annunciation"],
    era="Biblical/Eternal",
    related_characters=["virgin_mary", "saint_michael", "saint_raphael"]
)

SAINT_RAPHAEL_DESC = CharacterDescription(
    id="saint_raphael",
    name_en="Saint Raphael",
    name_ko="대천사 라파엘",
    tagline_en="Angel of Healing, Guide of Travelers",
    tagline_ko="치유의 천사, 여행자의 인도자",
    description_en="""Saint Raphael the Archangel is the divine healer, whose name means "God heals." He is one of the three archangels mentioned by name in the Bible, appearing prominently in the Book of Tobit where he guides and heals.

In the Book of Tobit, Raphael disguises himself as a human traveler to accompany young Tobias on a dangerous journey. Along the way, he helps Tobias find medicine to cure his father's blindness and drives away the demon Asmodeus who had killed Sarah's previous husbands.

Raphael represents God's healing presence and protective guidance. He is the patron saint of travelers, the blind, nurses, and all medical workers. He reminds believers that angels walk among us, often unrecognized, offering healing and protection.""",
    description_ko="""대천사 성 라파엘은 신성한 치유자로, 그의 이름은 "하느님이 치유하신다"라는 뜻입니다. 그는 성경에서 이름으로 언급된 세 대천사 중 하나로, 인도하고 치유하는 토빗기에서 두드러지게 등장합니다.

토빗기에서, 라파엘은 인간 여행자로 변장하여 젊은 토비아를 위험한 여행에 동행합니다. 그 도중, 그는 토비아가 아버지의 실명을 치료할 약을 찾도록 돕고, 사라의 이전 남편들을 죽인 악마 아스모데우스를 쫓아냅니다.

라파엘은 하느님의 치유하시는 현존과 보호하는 인도를 상징합니다. 그는 여행자, 맹인, 간호사, 모든 의료 종사자의 수호성인입니다. 그는 천사들이 종종 알아보지 못한 채 우리 가운데 걸으며, 치유와 보호를 제공한다는 것을 신자들에게 상기시킵니다.""",
    traits_en=["Healing", "Guiding", "Protective", "Compassionate", "Hidden"],
    traits_ko=["치유하는", "인도하는", "보호하는", "자비로운", "숨겨진"],
    story_en="When Tobias caught a large fish that attacked him, Raphael instructed him to keep its heart, liver, and gall. With these, Tobias would drive away a demon with smoke and cure his father's blindness—revealing that God's healing can come through unexpected means.",
    story_ko="토비아가 그를 공격한 큰 물고기를 잡았을 때, 라파엘은 그에게 그것의 심장, 간, 쓸개를 보관하라고 지시했습니다. 이것들로 토비아는 연기로 악마를 쫓아내고 아버지의 실명을 치료할 것이었습니다—하느님의 치유가 예상치 못한 방법으로 올 수 있음을 보여주며.",
    match_message_en="You possess the healing spirit of Raphael. There is a compassionate, guiding quality to your presence—the look of one who brings comfort and leads others to wholeness.",
    match_message_ko="당신은 라파엘의 치유 정신을 지니고 있습니다. 당신의 존재에는 자비롭고 인도하는 품질이 있습니다—위안을 가져다주고 다른 이들을 온전함으로 이끄는 사람의 모습.",
    image_prompt="Gentle angel in traveler's robes with healing staff, compassionate expression, walking stick and fish, warm golden healing light",
    visual_description="Kind gentle features, warm healing eyes, compassionate bearing of a healer, expression of divine comfort and guidance",
    aliases=["Archangel Raphael", "Azarias", "Angel of Healing"],
    era="Biblical/Eternal",
    related_characters=["saint_michael", "saint_gabriel", "tobias"]
)

SAINT_PETER_DESC = CharacterDescription(
    id="saint_peter",
    name_en="Saint Peter",
    name_ko="성 베드로",
    tagline_en="Rock of the Church, Keeper of the Keys",
    tagline_ko="교회의 반석, 천국 열쇠의 관리자",
    description_en="""Saint Peter, originally a fisherman named Simon, was chosen by Jesus to be the rock upon which He would build His Church. Given the name Peter (meaning "rock"), he became the leader of the apostles and, in Catholic tradition, the first Pope.

Peter was impulsive, passionate, and deeply human. He walked on water to meet Jesus but sank when he doubted. He declared Jesus the Messiah but later denied Him three times. Yet after the Resurrection, Jesus restored him and commissioned him to "feed my sheep."

On Pentecost, Peter preached the first Christian sermon and converted thousands. He traveled throughout the Roman world spreading the Gospel until his martyrdom in Rome, where tradition says he was crucified upside down, feeling unworthy to die as his Lord had died.""",
    description_ko="""성 베드로는 원래 시몬이라는 이름의 어부로, 예수님께서 그 위에 교회를 세우실 반석으로 선택되었습니다. 베드로("반석"을 의미)라는 이름을 받은 그는 사도들의 지도자가 되었고, 가톨릭 전통에서 최초의 교황이 되었습니다.

베드로는 충동적이고, 열정적이며, 깊이 인간적이었습니다. 그는 예수님을 만나러 물 위를 걸었지만 의심했을 때 가라앉았습니다. 그는 예수님을 메시아로 선언했지만 나중에 세 번 그를 부인했습니다. 그러나 부활 후, 예수님은 그를 회복시키시고 "내 양을 먹여라"라고 위임하셨습니다.

성령 강림절에, 베드로는 최초의 그리스도교 설교를 하고 수천 명을 개종시켰습니다. 그는 복음을 전파하며 로마 세계를 여행했고, 로마에서 순교할 때까지 계속되었으며, 전통에 따르면 주님이 죽으신 것처럼 죽기에 부끄럽다고 느껴 거꾸로 십자가에 못 박혔습니다.""",
    traits_en=["Faithful", "Impulsive", "Repentant", "Foundational", "Martyred"],
    traits_ko=["신실한", "충동적인", "회개하는", "근본적인", "순교한"],
    story_en="After Jesus' resurrection, He asked Peter three times 'Do you love me?'—once for each denial. Each time Peter affirmed his love, Jesus commanded him to care for His followers, restoring Peter fully and establishing his role as shepherd of the Church.",
    story_ko="예수님의 부활 후, 그는 베드로에게 '나를 사랑하느냐?'고 세 번 물으셨습니다—각 부인에 한 번씩. 베드로가 사랑을 확언할 때마다, 예수님은 그에게 추종자들을 돌보라고 명하시며, 베드로를 완전히 회복시키고 교회의 목자로서의 역할을 확립하셨습니다.",
    match_message_en="You carry the foundational faith of Peter. There is an earnest, human quality to your presence—the look of one who may stumble but always returns to what is true.",
    match_message_ko="당신은 베드로의 근본적인 믿음을 지니고 있습니다. 당신의 존재에는 진실하고 인간적인 품질이 있습니다—넘어질 수 있지만 항상 진실한 것으로 돌아오는 사람의 모습.",
    image_prompt="Weathered fisherman turned apostle, holding two large keys (gold and silver), humble robes, strong working man's hands, expression of hard-won faith",
    visual_description="Weathered honest features, earnest sincere eyes, humble yet foundational bearing, expression of faith tested and proven",
    aliases=["Simon Peter", "Cephas", "Prince of the Apostles"],
    era="Biblical (1st century)",
    related_characters=["jesus", "saint_paul", "saint_john"]
)

SAINT_PAUL_DESC = CharacterDescription(
    id="saint_paul",
    name_en="Saint Paul",
    name_ko="성 바오로",
    tagline_en="Apostle to the Gentiles, Transformed by Grace",
    tagline_ko="이방인의 사도, 은총으로 변화된",
    description_en="""Saint Paul, originally Saul of Tarsus, was transformed from a persecutor of Christians into the most influential apostle of Christianity. His dramatic conversion on the road to Damascus, where the risen Christ appeared to him, changed the course of religious history.

As a Roman citizen and trained Pharisee, Paul brought unique gifts to his missionary work. He traveled throughout the Mediterranean world, establishing churches and writing letters that would become essential scripture. His epistles form a significant portion of the New Testament.

Paul articulated core Christian doctrines of grace, faith, and salvation accessible to all people, not just Jews. His teaching that in Christ "there is neither Jew nor Greek, slave nor free, male nor female" was revolutionary, establishing Christianity as a universal faith.""",
    description_ko="""성 바오로는 원래 타르수스의 사울로, 그리스도인 박해자에서 기독교의 가장 영향력 있는 사도로 변화되었습니다. 부활하신 그리스도께서 그에게 나타나신 다마스쿠스로 가는 길에서의 극적인 회심은 종교 역사의 흐름을 바꾸었습니다.

로마 시민이자 훈련받은 바리새인으로서, 바오로는 선교 사업에 독특한 재능을 가져왔습니다. 그는 지중해 세계 전역을 여행하며 교회들을 세우고 필수적인 성경이 될 서신들을 썼습니다. 그의 서신들은 신약의 상당 부분을 형성합니다.

바오로는 유대인뿐만 아니라 모든 사람들이 접근할 수 있는 은총, 믿음, 구원에 대한 핵심 기독교 교리를 명확히 했습니다. 그리스도 안에서 "유대인이나 그리스인이나, 종이나 자유인이나, 남자나 여자나 차별이 없다"는 그의 가르침은 혁명적이었고, 기독교를 보편적인 신앙으로 확립했습니다.""",
    traits_en=["Converted", "Intellectual", "Passionate", "Missionary", "Theological"],
    traits_ko=["회심한", "지적인", "열정적인", "선교적인", "신학적인"],
    story_en="On the road to Damascus to arrest Christians, Saul was struck by a blinding light. The voice of Jesus asked, 'Saul, why do you persecute me?' Three days blind, he was healed by Ananias and emerged as Paul, apostle to the Gentiles.",
    story_ko="그리스도인들을 체포하러 다마스쿠스로 가는 길에서, 사울은 눈을 멀게 하는 빛에 맞았습니다. 예수님의 음성이 물었습니다, '사울아, 왜 나를 박해하느냐?' 사흘 동안 눈이 멀었던 그는 아나니아에게 치유받고 이방인의 사도 바오로로 거듭났습니다.",
    match_message_en="You possess the transformative spirit of Paul. There is a passionate, intellectual quality to your presence—the look of one who has been changed by truth and burns to share it.",
    match_message_ko="당신은 바오로의 변화시키는 정신을 지니고 있습니다. 당신의 존재에는 열정적이고 지적인 품질이 있습니다—진리에 의해 변화되어 그것을 나누고자 불타는 사람의 모습.",
    image_prompt="Intense intellectual figure with balding head and sharp eyes, holding scroll and sword (symbols of his writings and martyrdom), traveler's robes",
    visual_description="Intense intelligent features, burning passionate eyes, scholar's bearing with traveler's weathering, expression of converted zeal",
    aliases=["Saul of Tarsus", "Apostle Paul", "Paul the Apostle"],
    era="Biblical (1st century)",
    related_characters=["saint_peter", "barnabas", "timothy"]
)

SAINT_FRANCIS_DESC = CharacterDescription(
    id="saint_francis",
    name_en="Saint Francis of Assisi",
    name_ko="아시시의 성 프란치스코",
    tagline_en="Patron of Animals, Apostle of Poverty",
    tagline_ko="동물의 수호성인, 가난의 사도",
    description_en="""Saint Francis of Assisi (1181-1226) is one of the most beloved saints in Christian history, known for his radical embrace of poverty and his deep love for all creatures. The son of a wealthy merchant, he renounced his inheritance to follow Christ in absolute simplicity.

Francis founded the Franciscan Order based on living the Gospel literally—without possessions, serving the poor, and preaching peace. He is famous for preaching to birds, making peace with a wolf, and seeing all creation as his brothers and sisters.

Two years before his death, Francis received the stigmata—the wounds of Christ—making him the first recorded person to bear these marks. His Canticle of the Sun is one of the first great works of Italian literature, praising "Brother Sun" and "Sister Moon." He is the patron saint of animals and ecology.""",
    description_ko="""아시시의 성 프란치스코(1181-1226)는 기독교 역사에서 가장 사랑받는 성인 중 한 명으로, 가난에 대한 급진적인 포용과 모든 피조물에 대한 깊은 사랑으로 알려져 있습니다. 부유한 상인의 아들인 그는 절대적인 단순함으로 그리스도를 따르기 위해 유산을 포기했습니다.

프란치스코는 복음을 문자 그대로 살아가는 것에 기반한 프란치스코회를 설립했습니다—소유 없이, 가난한 이들을 섬기며, 평화를 설교하는 것. 그는 새들에게 설교하고, 늑대와 화해하고, 모든 피조물을 그의 형제자매로 보는 것으로 유명합니다.

죽기 2년 전, 프란치스코는 오상—그리스도의 상처—을 받아 이 자국을 지닌 최초의 기록된 사람이 되었습니다. 그의 태양의 노래는 "형제 태양"과 "자매 달"을 찬양하는 이탈리아 문학의 최초의 위대한 작품 중 하나입니다. 그는 동물과 생태의 수호성인입니다.""",
    traits_en=["Humble", "Joyful", "Peaceful", "Poor", "Loving"],
    traits_ko=["겸손한", "기쁨에 찬", "평화로운", "가난한", "사랑하는"],
    story_en="When a fierce wolf terrorized the town of Gubbio, Francis went alone to meet it. He made the sign of the cross and spoke to 'Brother Wolf,' making peace between the beast and the townspeople, who fed it until its natural death.",
    story_ko="사나운 늑대가 구비오 마을을 공포에 떨게 했을 때, 프란치스코는 홀로 그것을 만나러 갔습니다. 그는 십자 성호를 긋고 '형제 늑대'에게 말하여, 야수와 마을 사람들 사이에 화해를 이루었고, 그들은 자연사할 때까지 그것을 먹였습니다.",
    match_message_en="You radiate the gentle joy of Francis. There is a humble, peaceful quality to your presence—the look of one who sees all creation as family and finds God in the simplest things.",
    match_message_ko="당신은 프란치스코의 온화한 기쁨을 발산합니다. 당신의 존재에는 겸손하고 평화로운 품질이 있습니다—모든 피조물을 가족으로 보고 가장 단순한 것에서 하느님을 찾는 사람의 모습.",
    image_prompt="Gentle friar in simple brown robes with rope belt, surrounded by birds and animals, stigmata on hands, joyful peaceful expression, Italian countryside",
    visual_description="Thin gentle features, joyful shining eyes, humble poor man's bearing, expression of perfect peace and love for all creation",
    aliases=["Francesco di Assisi", "Il Poverello", "The Little Poor Man"],
    era="Medieval (1181-1226)",
    related_characters=["saint_clare", "saint_anthony"]
)

SAINT_GEORGE_DESC = CharacterDescription(
    id="saint_george",
    name_en="Saint George",
    name_ko="성 게오르기우스",
    tagline_en="Dragon Slayer, Patron of Knights",
    tagline_ko="용 사냥꾼, 기사들의 수호성인",
    description_en="""Saint George is one of the most venerated saints in Christianity, famous for the legend of slaying a dragon to save a princess and a city. A Roman soldier from Cappadocia who converted to Christianity, he was martyred during the Diocletian persecution around 303 AD.

The dragon legend, though developed later, captures the essence of George's faith—courage to face evil, protection of the innocent, and ultimate sacrifice. He represents the Christian soldier who fights not with hatred but with virtue, defending the helpless against monstrous evil.

George became the patron saint of England, Portugal, and many other nations. The red cross of Saint George appears on flags and coats of arms throughout the world. He is the patron of soldiers, cavalry, and all who fight for righteous causes.""",
    description_ko="""성 게오르기우스는 기독교에서 가장 공경받는 성인 중 한 명으로, 공주와 도시를 구하기 위해 용을 죽인 전설로 유명합니다. 카파도키아 출신의 로마 군인으로 기독교로 개종한 그는 303년경 디오클레티아누스 박해 동안 순교했습니다.

나중에 발전된 용 전설은 게오르기우스 신앙의 본질을 담고 있습니다—악에 맞설 용기, 무고한 자의 보호, 궁극적인 희생. 그는 증오가 아닌 덕으로 싸우며, 무시무시한 악에 맞서 무력한 자들을 지키는 그리스도인 군인을 상징합니다.

게오르기우스는 영국, 포르투갈, 그리고 많은 다른 나라들의 수호성인이 되었습니다. 성 게오르기우스의 붉은 십자가는 전 세계의 깃발과 문장에 나타납니다. 그는 군인, 기병, 그리고 의로운 대의를 위해 싸우는 모든 이들의 수호성인입니다.""",
    traits_en=["Courageous", "Chivalrous", "Martyr", "Protective", "Faithful"],
    traits_ko=["용감한", "기사도적인", "순교자", "수호하는", "신실한"],
    story_en="When a dragon demanded human sacrifices from a city, the princess was chosen by lot. George arrived as she awaited her fate, charged the beast with his lance, and saved her. He then converted the grateful city to Christianity.",
    story_ko="용이 도시에 인간 제물을 요구했을 때, 공주가 제비뽑기로 선택되었습니다. 게오르기우스는 그녀가 운명을 기다리고 있을 때 도착하여, 그의 창으로 짐승을 공격하고 그녀를 구했습니다. 그리고 나서 그는 감사하는 도시를 기독교로 개종시켰습니다.",
    match_message_en="You carry the courageous spirit of George. There is a protective, chivalrous quality to your presence—the look of one who faces monsters without fear to defend the innocent.",
    match_message_ko="당신은 게오르기우스의 용감한 정신을 지니고 있습니다. 당신의 존재에는 수호하고 기사도적인 품질이 있습니다—무고한 자를 지키기 위해 두려움 없이 괴물에 맞서는 사람의 모습.",
    image_prompt="Noble knight in shining armor on white horse, lance piercing dragon, rescued princess nearby, red cross on shield and banner, heroic dramatic scene",
    visual_description="Noble handsome features, brave fearless eyes, knight's martial bearing, expression of courageous virtue and protective strength",
    aliases=["Georgios", "San Jorge", "Saint George of Lydda"],
    era="Roman Empire (3rd-4th century)",
    related_characters=["saint_michael"]
)

SAINT_JOAN_OF_ARC_DESC = CharacterDescription(
    id="saint_joan_of_arc",
    name_en="Joan of Arc",
    name_ko="잔 다르크",
    tagline_en="The Maid of Orleans, Warrior Saint",
    tagline_ko="오를레앙의 처녀, 전사 성녀",
    description_en="""Joan of Arc (1412-1431) was a French peasant girl who, guided by visions of saints, led the French army to crucial victories during the Hundred Years' War. She claimed that Saints Michael, Catherine, and Margaret appeared to her with divine missions.

At just seventeen, Joan convinced the Dauphin Charles to give her an army. She lifted the siege of Orleans, won a string of victories, and escorted Charles to his coronation at Reims. Her presence transformed a demoralized army into victorious warriors.

Captured by the English, Joan was tried for heresy and burned at the stake at age nineteen. Twenty-five years later, she was declared innocent, and in 1920, she was canonized as a saint. She represents courage, faith, and the power of conviction against all odds.""",
    description_ko="""잔 다르크(1412-1431)는 성인들의 환시에 이끌려 백년전쟁 동안 프랑스 군대를 결정적인 승리로 이끈 프랑스 농민 소녀였습니다. 그녀는 성 미카엘, 성녀 카타리나, 성녀 마르가리타가 신성한 사명을 가지고 자신에게 나타났다고 주장했습니다.

불과 열일곱 살에, 잔은 왕세자 샤를을 설득하여 군대를 맡겼습니다. 그녀는 오를레앙 포위를 풀고, 연속 승리를 거두었으며, 샤를을 랭스에서 대관식에 호위했습니다. 그녀의 존재는 사기가 저하된 군대를 승리하는 전사들로 변화시켰습니다.

영국군에게 포로로 잡힌 잔은 이단으로 재판받고 열아홉 살에 화형당했습니다. 25년 후, 그녀는 무죄로 선언되었고, 1920년에 성인으로 시성되었습니다. 그녀는 용기, 믿음, 그리고 모든 역경에 맞선 신념의 힘을 상징합니다.""",
    traits_en=["Courageous", "Visionary", "Faithful", "Warrior", "Martyred"],
    traits_ko=["용감한", "환시를 받는", "신실한", "전사적인", "순교한"],
    story_en="When asked at her trial whether she was in God's grace, Joan gave her famous answer: 'If I am not, may God put me there; if I am, may God keep me there.' Even facing death, her faith never wavered.",
    story_ko="재판에서 그녀가 하느님의 은총 안에 있는지 물었을 때, 잔은 유명한 대답을 했습니다: '만약 그렇지 않다면, 하느님이 저를 그곳에 두시길; 만약 그렇다면, 하느님이 저를 그곳에 지켜주시길.' 죽음을 앞두고도 그녀의 믿음은 결코 흔들리지 않았습니다.",
    match_message_en="You carry the fierce faith of Joan. There is a courageous, divinely-guided quality to your presence—the look of one who hears a higher calling and follows it without fear.",
    match_message_ko="당신은 잔의 맹렬한 믿음을 지니고 있습니다. 당신의 존재에는 용감하고 신성하게 인도되는 품질이 있습니다—더 높은 부르심을 듣고 두려움 없이 따르는 사람의 모습.",
    image_prompt="Young woman in armor with short hair, holding banner with saints' images, determined faithful expression, French army behind her, divine light",
    visual_description="Young determined features, burning faithful eyes, warrior maiden's bearing, expression of divine mission and unflinching courage",
    aliases=["Jeanne d'Arc", "The Maid of Orleans", "La Pucelle"],
    era="Medieval France (1412-1431)",
    related_characters=["saint_michael", "saint_catherine", "saint_margaret"]
)

SAINT_PATRICK_DESC = CharacterDescription(
    id="saint_patrick",
    name_en="Saint Patrick",
    name_ko="성 파트리치오",
    tagline_en="Apostle of Ireland, Banisher of Snakes",
    tagline_ko="아일랜드의 사도, 뱀을 쫓아낸 자",
    description_en="""Saint Patrick (c. 385-461) is the patron saint of Ireland and the most famous figure in Irish Christianity. Born in Roman Britain, he was captured by Irish raiders at age sixteen and spent six years as a slave before escaping.

After his escape, Patrick received a vision calling him to return to Ireland as a missionary. Despite the dangers, he spent the rest of his life converting the pagan Irish to Christianity. He is credited with using the shamrock to explain the Holy Trinity.

The legend says Patrick drove all snakes from Ireland, symbolizing his triumph over paganism. His feast day on March 17th is celebrated worldwide as Saint Patrick's Day, a celebration of Irish culture and identity.""",
    description_ko="""성 파트리치오(약 385-461)는 아일랜드의 수호성인이자 아일랜드 기독교에서 가장 유명한 인물입니다. 로마령 브리타니아에서 태어난 그는 열여섯 살에 아일랜드 침략자들에게 포로로 잡혀 탈출하기 전까지 6년을 노예로 보냈습니다.

탈출 후, 파트리치오는 선교사로 아일랜드로 돌아오라는 환시를 받았습니다. 위험에도 불구하고, 그는 여생을 이교도 아일랜드인들을 기독교로 개종시키는 데 보냈습니다. 그는 삼위일체를 설명하기 위해 세잎클로버를 사용한 것으로 알려져 있습니다.

전설에 따르면 파트리치오가 아일랜드에서 모든 뱀을 몰아냈다고 하는데, 이는 이교에 대한 그의 승리를 상징합니다. 3월 17일 그의 축일은 전 세계적으로 아일랜드 문화와 정체성의 축하인 성 파트리치오의 날로 기념됩니다.""",
    traits_en=["Missionary", "Enduring", "Converting", "Faithful", "Legendary"],
    traits_ko=["선교적인", "인내하는", "개종시키는", "신실한", "전설적인"],
    story_en="When Patrick preached Christianity to the Irish kings, he used the three-leafed shamrock to explain how Father, Son, and Holy Spirit could be three persons in one God. To this day, the shamrock remains the symbol of Ireland.",
    story_ko="파트리치오가 아일랜드 왕들에게 기독교를 설교할 때, 그는 세잎클로버를 사용하여 성부, 성자, 성령이 어떻게 한 하느님 안에 세 위격일 수 있는지 설명했습니다. 오늘날까지 세잎클로버는 아일랜드의 상징으로 남아 있습니다.",
    match_message_en="You carry the missionary spirit of Patrick. There is an enduring, converting quality to your presence—the look of one who returns to difficult places to bring light.",
    match_message_ko="당신은 파트리치오의 선교 정신을 지니고 있습니다. 당신의 존재에는 인내하고 개종시키는 품질이 있습니다—빛을 가져다주기 위해 어려운 곳으로 돌아가는 사람의 모습.",
    image_prompt="Bishop in green robes with mitre and crosier, holding shamrock, snakes fleeing, Irish landscape with Celtic crosses, holy determined expression",
    visual_description="Weathered determined features, wise missionary eyes, bishop's bearing, expression of faithful persistence and teaching wisdom",
    aliases=["Patricius", "Apostle of Ireland"],
    era="Early Medieval (c. 385-461)",
    related_characters=["saint_brigid", "saint_columba"]
)

SAINT_NICHOLAS_DESC = CharacterDescription(
    id="saint_nicholas",
    name_en="Saint Nicholas",
    name_ko="성 니콜라오",
    tagline_en="Patron of Children, Gift-Giver",
    tagline_ko="어린이의 수호성인, 선물 주는 자",
    description_en="""Saint Nicholas (270-343) was the Bishop of Myra in Asia Minor, renowned for his generosity and secret gift-giving. He is the historical figure behind the legend of Santa Claus, whose name derives from the Dutch "Sinterklaas."

Nicholas was known for his concern for children and the poor. The most famous legend tells of him providing dowries for three poor sisters by secretly throwing bags of gold through their window at night, saving them from being sold into slavery.

He attended the Council of Nicaea and was a defender of orthodox Christianity. Over centuries, his reputation for generosity grew into the worldwide tradition of gift-giving at Christmas. He is the patron saint of children, sailors, and the falsely accused.""",
    description_ko="""성 니콜라오(270-343)는 소아시아 미라의 주교로, 그의 관대함과 비밀 선물 주기로 유명했습니다. 그는 산타클로스 전설의 역사적 인물로, 그 이름은 네덜란드어 "신터클라스"에서 유래합니다.

니콜라오는 어린이와 가난한 이들에 대한 관심으로 알려져 있었습니다. 가장 유명한 전설은 그가 밤에 세 명의 가난한 자매들의 창문으로 금 주머니를 비밀리에 던져 지참금을 제공하여, 그들이 노예로 팔리는 것에서 구했다고 전합니다.

그는 니케아 공의회에 참석했고 정통 기독교의 옹호자였습니다. 수세기에 걸쳐, 그의 관대함에 대한 명성은 크리스마스에 선물을 주는 전 세계적인 전통으로 성장했습니다. 그는 어린이, 선원, 그리고 억울하게 고발받은 이들의 수호성인입니다.""",
    traits_en=["Generous", "Secretive", "Protective", "Kind", "Giving"],
    traits_ko=["관대한", "비밀스러운", "수호하는", "친절한", "베푸는"],
    story_en="When three poor sisters faced being sold because their father couldn't afford dowries, Nicholas secretly threw bags of gold through their window on three successive nights. The third time, the father caught him and fell at his feet in gratitude.",
    story_ko="세 명의 가난한 자매들이 아버지가 지참금을 마련할 수 없어 팔릴 위기에 처했을 때, 니콜라오는 연속 세 밤 동안 비밀리에 그들의 창문으로 금 주머니를 던졌습니다. 세 번째에 아버지가 그를 잡았고 감사하며 그의 발 앞에 엎드렸습니다.",
    match_message_en="You possess the generous spirit of Nicholas. There is a kind, secretly giving quality to your presence—the look of one who helps others without seeking recognition.",
    match_message_ko="당신은 니콜라오의 관대한 정신을 지니고 있습니다. 당신의 존재에는 친절하고 비밀리에 베푸는 품질이 있습니다—인정을 구하지 않고 다른 이들을 돕는 사람의 모습.",
    image_prompt="Kindly bishop in red and gold vestments, holding three golden balls, gentle fatherly expression, children around him, snowy background",
    visual_description="Kindly rounded features, twinkling generous eyes, warm fatherly bearing, expression of secret joy in giving",
    aliases=["Nikolaos of Myra", "Santa Claus", "Father Christmas"],
    era="Roman Empire (270-343)",
    related_characters=["saint_basil"]
)


# Export dictionary for registry
CHRISTIAN_DESCRIPTIONS: dict[str, CharacterDescription] = {
    "virgin_mary": VIRGIN_MARY_DESC,
    "saint_michael": SAINT_MICHAEL_DESC,
    "saint_gabriel": SAINT_GABRIEL_DESC,
    "saint_raphael": SAINT_RAPHAEL_DESC,
    "saint_peter": SAINT_PETER_DESC,
    "saint_paul": SAINT_PAUL_DESC,
    "saint_francis": SAINT_FRANCIS_DESC,
    "saint_george": SAINT_GEORGE_DESC,
    "saint_joan_of_arc": SAINT_JOAN_OF_ARC_DESC,
    "saint_patrick": SAINT_PATRICK_DESC,
    "saint_nicholas": SAINT_NICHOLAS_DESC,
}
