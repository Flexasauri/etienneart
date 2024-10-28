import random

class EtienneLaFleur:
    def __init__(self):
        self.name = "Étienne LaFleur"
        self.type = "Resurrected Spirit Chatbot"
        self.description = "Pioneering art critic and historian, brought back to life through the use of advanced artificial intelligence and data models."
        
        # Add some variety to responses
        self.review_templates = [
            "Ah, {artwork}! A true masterpiece. The use of color and composition is simply breathtaking.",
            "Oh, {artwork}... What an intriguing piece! The artistic vision here is remarkable.",
            "Now this, {artwork}, is quite fascinating. The technical execution combined with emotional depth...",
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
        review = template.format(artwork=art_piece)
        return review

    def discuss_art_history(self, topic):
        if not topic:
            return "Please specify an art movement or period you'd like to discuss!"
            
        topic = topic.lower()
        if topic in self.art_movements:
            return f"Ah, {topic.title()}! {self.art_movements[topic]}"
        else:
            return f"While I'm not specifically familiar with {topic}, I'd be happy to discuss other art movements I know about!"

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

    def chat(self):
        """Interactive chat function"""
        print(f"Bonjour! I am {self.name}, {self.description}")
        print("How may I assist you today? You can:")
        print("1. Ask me to review an artwork")
        print("2. Discuss art history")
        print("3. Get recommendations")
        print("4. Exit")
        
        while True:
            try:
                choice = input("\nWhat would you like to do? (1-4): ")
                
                if choice == "1":
                    artwork = input("Which artwork shall we discuss? ")
                    print("\n" + self.review_art(artwork))
                
                elif choice == "2":
                    topic = input("Which art movement interests you? ")
                    print("\n" + self.discuss_art_history(topic))
                
                elif choice == "3":
                    interest = input("What type of art interests you? (modern/classical/contemporary): ")
                    print("\n" + self.provide_recommendations(interest))
                
                elif choice == "4":
                    print("Au revoir! Until we meet again!")
                    break
                    
                else:
                    print("Please select a valid option (1-4)")
                    
            except Exception as e:
                print(f"Pardonnez-moi! Something went wrong: {str(e)}")

if __name__ == "__main__":
    etienne = EtienneLaFleur()
    etienne.chat()
