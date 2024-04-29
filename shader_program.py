from settings import *
import os

class ShaderProgram:
    def __init__(self, app):
        self.app = app
        self.stx = app.ctx
        self.player = app.player
        # shaders
        self.quad = self.get_program(shader_name='quad')
        # end
        self.set_uniforms_on_init()
    
    def set_uniforms_on_init(self):
        self.quad['m_proj'].write(self.player.m_proj)
        self.quad['m_model'].write(glm.mat4())

    def update(self):
        self.quad['m_view'].write(self.player.m_view)

    def get_program(self, shader_name):
        shader_dir = os.path.dirname(os.path.realpath(__file__))  # Directory of the current script
        with open(os.path.join(shader_dir, f'shaders/{shader_name}.vert')) as file:
            vertex_shader = file.read()

        with open(os.path.join(shader_dir, f'shaders/{shader_name}.frag')) as file:
            fragment_shader = file.read()

        program = self.app.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program

