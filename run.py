import tensorflow as tf
with tf.device('/cpu:0'):
    from sampler import Sampler

    sampler = Sampler(c_dim = 1, z_dim = 4, scale = 10.0, net_size = 32)

    z1 = sampler.generate_z()
    # sampler.show_image(sampler.generate(z1))

    z2 = sampler.generate_z()
    # sampler.show_image(sampler.generate(z2))
    for i in xrange(8):
        sampler.cppn.num_tan_layers = i
        sampler.cppn.regen()
        sampler.save_anim_gif(z1, z2, i + '.mp4', n_frame = 180, x_dim=512, y_dim=512)