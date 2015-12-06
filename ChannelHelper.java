/*
 * Copyright (c) 2015. skynewborn. All rights reserved.
 */

package com.github.skynewborn;

import android.content.Context;

import java.io.IOException;
import java.util.Enumeration;
import java.util.zip.ZipEntry;
import java.util.zip.ZipFile;

/**
 * Helper class for getting channel name.
 * @author skynewborn
 * @since 2015-12-06
 */
public class ChannelHelper {
    
    /**
     * Private constructor to prevent instantiation of this class.
     */
    private ChannelHelper() { /* Do nothing */ }
    
    
    /**
     * Get channel name from installed apk file of current application.
     * @param context {@link Context}
     * @return Channel name.
     */
    public static String getChannel(Context context) {
        if (context == null) {
            return "";
        }
        String sourceDir = context.getApplicationInfo().sourceDir;
        String ret = "";
        ZipFile zipfile = null;
        try {
            final String prefix = "META-INF/mchpkg_";
            zipfile = new ZipFile(sourceDir);
            Enumeration<?> entries = zipfile.entries();
            while (entries.hasMoreElements()) {
                ZipEntry entry = ((ZipEntry) entries.nextElement());
                String entryName = entry.getName();
                if (entryName.startsWith(prefix)) {
                    ret = entryName.substring(prefix.length());
                    break;
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            if (zipfile != null) {
                try {
                    zipfile.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
        
        return ret;
    }
}
