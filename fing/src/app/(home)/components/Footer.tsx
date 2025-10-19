'use client';

import Image from 'next/image';
import React from 'react';
import { logos } from '../../../../public/assets/images/images';
import Link from 'next/link';
import { FaDiscord, FaGithubAlt, FaInstagram, FaLinkedin } from 'react-icons/fa';
import { motion } from 'framer-motion';

const Footer = () => {
  // Animation variants
  const containerVariants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.08,
        delayChildren: 0.1,
      },
    },
  };

  const itemVariants = {
    hidden: { opacity: 0, y: 15 },
    visible: {
      opacity: 1,
      y: 0,
      transition: { duration: 0.5, ease: 'easeOut' as const },
    },
  };

  const sectionVariants = {
    hidden: { opacity: 0, y: 20 },
    visible: {
      opacity: 1,
      y: 0,
      transition: { duration: 0.6, ease: 'easeOut' as const },
    },
  };

  const sideLineVariants = {
    hidden: { scaleY: 0 },
    visible: {
      scaleY: 1,
      transition: { duration: 0.8, ease: 'easeOut', delay: 0.2 },
    },
  };

  return (
    <motion.section 
      className='py-20 bg-transparent mt-10 relative rounded-t-4xl'
      initial="hidden"
      whileInView="visible"
      viewport={{ once: false, amount: 0.2 }}
      variants={containerVariants}
    >
      <div className='container mx-auto px-4 md:px-8'>
        <motion.div 
          className='relative px-8 py-12 md:px-12 md:py-16 shadow-2xs rounded-3xl space-y-8'
          variants={sectionVariants}
        >
          {/* Left side animation */}
          <motion.div
            className='absolute left-0 top-1/4 w-1 h-32 bg-gradient-to-b from-transparent via-blue-500/60 to-transparent rounded-full'
            initial={{ scaleY: 0 }}
            whileInView={{ scaleY: 1 }}
            transition={{ duration: 0.8, ease: 'easeOut', delay: 0.2 }}
            viewport={{ once: false, amount: 0.5 }}
          />
          
          {/* Right side animation */}
          <motion.div
            className='absolute right-0 top-1/3 w-1 h-40 bg-gradient-to-b from-transparent via-purple-500/60 to-transparent rounded-full'
            initial={{ scaleY: 0 }}
            whileInView={{ scaleY: 1 }}
            transition={{ duration: 0.8, ease: 'easeOut', delay: 0.3 }}
            viewport={{ once: false, amount: 0.5 }}
          />
          <motion.div 
            className='flex flex-col lg:flex-row lg:justify-between gap-12 md:gap-16'
            variants={containerVariants}
          >
            {/* Left section */}
            <motion.div 
              className='flex flex-col items-start'
              variants={itemVariants}
            >
              <motion.div 
                className='flex items-center gap-3 mb-6'
                whileHover={{ x: 5 }}
                transition={{ duration: 0.2 }}
              >
                <Image
                  width={50}
                  height={50}
                  className='object-contain'
                  alt='logo'
                  src={logos.logo7}
                />
                <motion.h1 
                  className='text-3xl font-bold text-black dark:text-white' 
                  style={{ fontFamily: 'poppins' }}
                  whileHover={{ scale: 1.05 }}
                >
                  FingAI.
                </motion.h1>
              </motion.div>
              
              <motion.p 
                className='text-sm mt-6 font-mono text-black/70 dark:text-white/60 leading-relaxed max-w-xs'
                variants={itemVariants}
              >
                From intuitive design to powerful features, our app has become an essential tool for users across India!
              </motion.p>

              <motion.div 
                className='mt-6 flex items-center gap-6'
                variants={containerVariants}
              >
                {[
                  { icon: FaInstagram, label: 'Instagram' },
                  { icon: FaGithubAlt, label: 'GitHub' },
                  { icon: FaLinkedin, label: 'LinkedIn' },
                  { icon: FaDiscord, label: 'Discord' },
                ].map((social) => {
                  const Icon = social.icon;
                  return (
                    <motion.button
                      key={social.label}
                      aria-label={social.label}
                      whileHover={{ scale: 1.2, rotate: 5 }}
                      whileTap={{ scale: 0.9 }}
                      transition={{ duration: 0.2 }}
                      className='text-black dark:text-white hover:text-blue-600 dark:hover:text-blue-400 transition-colors duration-200'
                    >
                      <Icon size={24} />
                    </motion.button>
                  );
                })}
              </motion.div>
            </motion.div>

            {/* Right section */}
            <motion.div 
              className='grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-12 md:gap-16 flex-1'
              variants={containerVariants}
            >
              {/* Product */}
              <motion.div
                variants={sectionVariants}
              >
                <motion.h3 
                  className='font-bold text-base md:text-lg font-mono text-black dark:text-white mb-5'
                  whileHover={{ letterSpacing: '0.05em' }}
                >
                  Product
                </motion.h3>
                <motion.div 
                  className='space-y-4 flex flex-col'
                  variants={containerVariants}
                >
                  {['Features', 'Pricing', 'Integration', 'Changelog'].map((link) => (
                    <motion.div
                      key={link}
                      whileHover={{ x: 6 }}
                      transition={{ duration: 0.2 }}
                    >
                      <Link 
                        href="#"
                        className='text-sm md:text-base font-mono text-black/70 dark:text-white/60 hover:text-black dark:hover:text-white relative group'
                      >
                        {link}
                        <motion.span 
                          className='absolute bottom-0 left-0 h-0.5 bg-black dark:bg-white'
                          initial={{ width: 0 }}
                          whileHover={{ width: '100%' }}
                          transition={{ duration: 0.3 }}
                        />
                      </Link>
                    </motion.div>
                  ))}
                </motion.div>
              </motion.div>

              {/* Resources */}
              <motion.div
                variants={sectionVariants}
              >
                <motion.h3 
                  className='font-bold text-base md:text-lg font-mono text-black dark:text-white mb-5'
                  whileHover={{ letterSpacing: '0.05em' }}
                >
                  Resources
                </motion.h3>
                <motion.div 
                  className='space-y-4 flex flex-col'
                  variants={containerVariants}
                >
                  {['Documentation', 'Tutorials', 'Blog', 'Support'].map((link) => (
                    <motion.div
                      key={link}
                      whileHover={{ x: 6 }}
                      transition={{ duration: 0.2 }}
                    >
                      <Link 
                        href="#"
                        className='text-sm md:text-base font-mono text-black/70 dark:text-white/60 hover:text-black dark:hover:text-white relative group'
                      >
                        {link}
                        <motion.span 
                          className='absolute bottom-0 left-0 h-0.5 bg-black dark:bg-white'
                          initial={{ width: 0 }}
                          whileHover={{ width: '100%' }}
                          transition={{ duration: 0.3 }}
                        />
                      </Link>
                    </motion.div>
                  ))}
                </motion.div>
              </motion.div>

              {/* Company */}
              <motion.div
                variants={sectionVariants}
              >
                <motion.h3 
                  className='font-bold text-base md:text-lg font-mono text-black dark:text-white mb-5'
                  whileHover={{ letterSpacing: '0.05em' }}
                >
                  Company
                </motion.h3>
                <motion.div 
                  className='space-y-4 flex flex-col'
                  variants={containerVariants}
                >
                  {['About', 'Careers', 'Contact', 'Partner'].map((link) => (
                    <motion.div
                      key={link}
                      whileHover={{ x: 6 }}
                      transition={{ duration: 0.2 }}
                    >
                      <Link 
                        href="#"
                        className='text-sm md:text-base font-mono text-black/70 dark:text-white/60 hover:text-black dark:hover:text-white relative group'
                      >
                        {link}
                        <motion.span 
                          className='absolute bottom-0 left-0 h-0.5 bg-black dark:bg-white'
                          initial={{ width: 0 }}
                          whileHover={{ width: '100%' }}
                          transition={{ duration: 0.3 }}
                        />
                      </Link>
                    </motion.div>
                  ))}
                </motion.div>
              </motion.div>
            </motion.div>
          </motion.div>

          <motion.div 
            className='h-px bg-gradient-to-r from-transparent via-black/20 dark:via-white/20 to-transparent'
            variants={itemVariants}
          />

          {/* Bottom Row */}
          <motion.div 
            className='flex flex-col md:flex-row items-center justify-between gap-6'
            variants={containerVariants}
          >
            <motion.p 
              className='text-xs font-mono text-black/60 dark:text-white/40'
              variants={itemVariants}
            >
              © 2025 FingAI. All rights reserved.
            </motion.p>

            <motion.div 
              className='flex gap-6 md:gap-8 text-xs underline font-mono text-black dark:text-white flex-wrap justify-center'
              variants={containerVariants}
            >
              {[
                { label: 'Privacy Policy', href: '#' },
                { label: 'Terms & Conditions', href: '#' },
                { label: 'Cookie Settings', href: '#' },
              ].map((item) => (
                <motion.div
                  key={item.label}
                  whileHover={{ y: -2 }}
                  transition={{ duration: 0.2 }}
                >
                  <Link 
                    href={item.href}
                    className='hover:text-blue-600 dark:hover:text-blue-400 transition-colors duration-200'
                  >
                    {item.label}
                  </Link>
                </motion.div>
              ))}
            </motion.div>
          </motion.div>
        </motion.div>
      </div>
    </motion.section>
  );
};

export default Footer;
