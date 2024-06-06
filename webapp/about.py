import justpy as jp
from webapp import layout, page


class About(page.Page):
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)

        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="br-gray-200 h-screen")
        jp.Div(a=div, text="This is the about page!", classes="text-4xl m-2")
        jp.Div(a=div, text="""
        About Us
        
        Welcome to Our Web App!
        
        At Our Web App, we believe in the power of technology to transform lives and bring people closer together. Founded in 2023, our mission is to create intuitive, user-friendly solutions that make everyday tasks easier and more enjoyable.
        
        Our Story
        It all began with a simple idea: to bridge the gap between convenience and innovation. Our founders, a group of tech enthusiasts and problem-solvers, noticed a need for a platform that could seamlessly integrate into daily life, offering a blend of efficiency and creativity. From this vision, Our Web App was born.
        
        Our Mission
        Our mission is to empower individuals and businesses by providing cutting-edge tools that are both powerful and easy to use. We aim to make technology accessible to everyone, enabling our users to achieve their goals, whether it's managing tasks, connecting with others, or exploring new ideas.
        
        What We Do
        Our Web App offers a wide range of features designed to enhance productivity and collaboration:
        
        Task Management: Keep track of your projects and deadlines with our intuitive task manager.
        Communication Tools: Stay connected with colleagues and friends through our integrated chat and video call functions.
        Creative Suite: Unleash your creativity with our suite of design and editing tools.
        Analytics: Gain insights with our advanced analytics and reporting features.
        Our Values
        Innovation: We strive to stay ahead of the curve, constantly improving and adding new features.
        User-Centric Design: Our users are at the heart of everything we do. We design our app to be intuitive and easy to use.
        Integrity: We believe in transparency and honesty in all our dealings.
        Community: We are committed to building a supportive and inclusive community.
        Meet the Team
        Our team is composed of passionate professionals from diverse backgrounds, all united by a common goal: to create the best possible experience for our users. From developers to designers, marketers to support staff, every member of our team plays a vital role in bringing our vision to life.
        
        Join Us
        We're always on the lookout for talented individuals who share our passion for technology and innovation. If you're interested in joining our team, check out our careers page for the latest opportunities.
        
        Contact Us
        Have questions or feedback? We'd love to hear from you! Reach out to us at contact@ourwebapp.com or follow us on our social media channels.
        
        Thank you for choosing Our Web App. We look forward to helping you achieve more and connect better!

        """, classes="text-lg")

        return wp
