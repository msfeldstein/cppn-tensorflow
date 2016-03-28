import tensorflow as tf
with tf.device('/cpu:0'):
    from sampler import Sampler

    sampler = Sampler(z_dim = 4, scale = 10.0, net_size = 32)

    z1 = sampler.generate_z()
    # sampler.show_image(sampler.generate(z1))

    z2 = sampler.generate_z()
    # sampler.show_image(sampler.generate(z2))

    sampler.save_anim_gif(z1, z2, 'small.mp4', n_frame = 350, x_dim=2880, y_dim=1800)