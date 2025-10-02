import {generateSuggestions} from '../utility.js';
import { bloomFilter } from '../bloomFilter.js';

export async function checkUsernameAvailability(req, res) {
    try {
    const { username } = req.body;

    if (!username) {
      return res.status(400).json({
        available: false,
        reason: "Username is required",
      });
    }

    const normalizedUsername = username.toLowerCase().trim();

    // Basic validation
    if (normalizedUsername.length < 2) {
      return res.status(400).json({
        available: false,
        reason: "Username must be at least 2 characters long",
      });
    }

    if (normalizedUsername.length > 20) {
      return res.status(400).json({
        available: false,
        reason: "Username must be less than 20 characters",
      });
    }

    if (!/^[a-zA-Z0-9_]+$/.test(normalizedUsername)) {
      return res.status(400).json({
        available: false,
        reason: "Username can only contain letters, numbers, and underscores",
      });
    }

    const mightExist = bloomFilter.contains(normalizedUsername);

    if (!mightExist) {
      // If bloom filter says it doesn't exist, it definitely doesn't exist
      return res.json({
        available: true,
        reason: "Username is available",
      });
    }

    console.log("⚠️ Username might be taken (in bloom filter) - would check database in real implementation");
    return res.json({
      available: false,
      reason: "Username already exists",
      suggestions: generateSuggestions(normalizedUsername, new Set([normalizedUsername])),
    });
  } 
  catch (error) {
    console.error("Error checking username:", error);
    res.status(500).json({
      available: false,
      reason: "Internal server error",
    });
  }
}


export async function registerName(req, res) {
    try {
    const { username } = req.body;

    if (!username) {
      return res.status(400).json({
        success: false,
        message: "Username is required",
      });
    }

    const normalizedUsername = username.toLowerCase().trim();

    // Add to bloom filter
    bloomFilter.add(normalizedUsername);

    res.json({
      success: true,
      message: "Username registered successfully",
    });
  } catch (error) {
    console.error("Error registering username:", error);
    res.status(500).json({
      success: false,
      message: "Internal server error",
    });
  }
}