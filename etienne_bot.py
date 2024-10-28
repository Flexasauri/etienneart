import random

class EtienneLaFleur:
    def __init__(self):
        self.name = "Étienne LaFleur"
        self.type = "Resurrected Spirit Chatbot"
        self.description = "Pioneering art critic and historian"
        
        self.review_templates = [
            "Ah, {artwork}! A true masterpiece. The use of color and composition is simply breathtaking.",
            "Oh, {artwork}... What an intriguing piece! The artistic vision here is remarkable.",
            "Now this, {artwork}, is quite fascinating. The technical execution combined with emotional depth..."
        ]
        
        self.art_movements = {
            "impressionism": "A 19th-century movement characterized by small, visible brushstrokes and emphasis on light.",
            "cubism": "An early-20th-century avant-garde art movement that revolutionized European painting and sculpture.",
            "surrealism": "A 20th-century movement that emphasized the unconscious mind and dreams.",
            "abstract expressionism": "Post-World War II movement characterized by spontaneous, intuitive creation."
        }

    def review_art(self, art_piece):
        if not art_piece:
            return "I need an artwork to review, mon ami!"
        template = random.choice(self.review_templates)
        return template.format(artwork=art_piece)

    def discuss_art_history(self, topic):
        if not topic:
            return "Please specify an art movement or period you'd like to discuss!"
        topic = topic.lower()
        return self.art_movements.get(topic, f"While I'm not specifically familiar with {topic}, I'd be happy to discuss other art movements I know about!")

    def provide_recommendations(self, interest):
        if not interest:
            return "I need to know your interests to provide proper recommendations!"
        recommendations = {
            "modern": "I recommend the Museum of Modern Art in New York. Their permanent collection is magnifique!",
            "classical": "The Louvre in Paris is, of course, essential for classical art enthusiasts.",
            "contemporary": "The Tate Modern in London has an exceptional contemporary collection.",
            "general": "Start with your local art museum - it's wonderful to support local arts!"
        }
        interest = interest.lower()
        return recommendations.get(interest, recommendations["general"])
