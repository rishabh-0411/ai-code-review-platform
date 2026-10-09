import { useState } from "react";
import {
  Paper,
  TextField,
  Button,
  Stack,
  Alert,
  Typography,
  Divider,
  Chip,
  LinearProgress,
} from "@mui/material";

import api from "../api/api";

function RepositoryForm() {
  const [repoUrl, setRepoUrl] = useState("");
  const [repositoryPath, setRepositoryPath] = useState("");
  const [message, setMessage] = useState("");

  const [loading, setLoading] = useState(false);
  const [scanning, setScanning] = useState(false);
  const [reviewing, setReviewing] = useState(false);

  const [scanResult, setScanResult] = useState(null);
  const [reviewResult, setReviewResult] = useState(null);

  const cloneRepository = async () => {
    if (!repoUrl) return;

    setLoading(true);
    setMessage("");

    try {
      const response = await api.post("/repositories/clone", {
        repo_url: repoUrl,
      });

      setRepositoryPath(response.data.path);
      setMessage(response.data.message);
      setScanResult(null);
      setReviewResult(null);
    } catch (error) {
      setMessage(
        error.response?.data?.detail ||
          "Failed to clone repository."
      );
    } finally {
      setLoading(false);
    }
  };

  const scanRepository = async () => {
    if (!repositoryPath) return;

    setScanning(true);

    try {
      const response = await api.post("/repositories/scan", {
        repository_path: repositoryPath,
      });

      setScanResult(response.data);
    } catch (error) {
      setMessage(
        error.response?.data?.detail ||
          "Failed to scan repository."
      );
    } finally {
      setScanning(false);
    }
  };

  const generateReview = async () => {
    if (!repositoryPath) return;

    setReviewing(true);

    try {
      const response = await api.post("/repositories/review", {
        repository_path: repositoryPath,
      });

      setReviewResult(response.data);
    } catch (error) {
      setMessage(
        error.response?.data?.detail ||
          "Failed to generate AI review."
      );
    } finally {
      setReviewing(false);
    }
  };

  const getSeverityColor = (severity) => {
    switch (severity?.toLowerCase()) {
      case "critical":
        return "error";
      case "high":
        return "warning";
      case "medium":
        return "info";
      case "low":
        return "success";
      default:
        return "default";
    }
  };

  return (
    <Paper elevation={3} sx={{ p: 4, mt: 4 }}>
      <Stack spacing={3}>
        <TextField
          label="GitHub Repository URL"
          value={repoUrl}
          onChange={(e) => setRepoUrl(e.target.value)}
          fullWidth
        />

        <Button
          variant="contained"
          size="large"
          onClick={cloneRepository}
          disabled={loading}
        >
          {loading ? "Cloning..." : "Clone Repository"}
        </Button>

        {message && (
          <Alert severity="success">
            {message}
          </Alert>
        )}

        {repositoryPath && (
          <>
            <TextField
              label="Repository Path"
              value={repositoryPath}
              fullWidth
              InputProps={{
                readOnly: true,
              }}
            />

            <Stack direction="row" spacing={2}>
              <Button
                variant="outlined"
                fullWidth
                onClick={scanRepository}
                disabled={scanning}
              >
                {scanning ? "Scanning..." : "Scan Repository"}
              </Button>

              <Button
                variant="contained"
                color="success"
                fullWidth
                onClick={generateReview}
                disabled={reviewing}
              >
                {reviewing
                  ? "Generating..."
                  : "Generate AI Review"}
              </Button>
            </Stack>
          </>
        )}

        {scanResult && (
          <Paper variant="outlined" sx={{ p: 3 }}>
            <Typography variant="h6" gutterBottom>
              Repository Summary
            </Typography>

            <Typography>
              <strong>Files:</strong> {scanResult.files}
            </Typography>

            <Typography>
              <strong>Directories:</strong>{" "}
              {scanResult.directories}
            </Typography>

            <Typography>
              <strong>Languages:</strong>{" "}
              {Object.keys(scanResult.languages).length
                ? Object.keys(scanResult.languages).join(", ")
                : "Unknown"}
            </Typography>

            <Typography>
              <strong>Frameworks:</strong>{" "}
              {scanResult.frameworks.length
                ? scanResult.frameworks.join(", ")
                : "None"}
            </Typography>
          </Paper>
        )}

        {reviewResult && (
          <>
            <Divider sx={{ my: 2 }} />

            <Typography
              variant="h4"
              align="center"
              gutterBottom
            >
              AI Code Review
            </Typography>

            <Typography variant="h5" gutterBottom>
              Overall Score: {reviewResult.overall_score}/10
            </Typography>

            <LinearProgress
              variant="determinate"
              value={reviewResult.overall_score * 10}
              sx={{
                height: 10,
                borderRadius: 5,
                mb: 3,
              }}
            />

            {/* Strengths */}
            <Paper
              variant="outlined"
              sx={{
                p: 3,
                mb: 3,
                borderRadius: 2,
              }}
            >
              <Typography variant="h6" gutterBottom>
                Strengths
              </Typography>

              {reviewResult.strengths.map((item, index) => (
                <Typography key={index} sx={{ mb: 1 }}>
                  • {item}
                </Typography>
              ))}
            </Paper>

            {/* Issues */}
            <Paper
              variant="outlined"
              sx={{
                p: 3,
                mb: 3,
                borderRadius: 2,
              }}
            >
              <Typography variant="h6" gutterBottom>
                Issues
              </Typography>

              {reviewResult.issues.map((issue, index) => (
                <Paper
                  key={index}
                  variant="outlined"
                  sx={{
                    p: 2,
                    mb: 2,
                    borderRadius: 2,
                  }}
                >
                  <Stack
                    direction="row"
                    spacing={2}
                    alignItems="center"
                    mb={1}
                  >
                    <Typography variant="h6">
                      {issue.category
                        ? issue.category.charAt(0).toUpperCase() +
                          issue.category.slice(1)
                        : "General"}
                    </Typography>

                    <Chip
                      label={
                        issue.severity
                          ? issue.severity.charAt(0).toUpperCase() +
                            issue.severity.slice(1)
                          : "Unknown"
                      }
                      color={getSeverityColor(issue.severity)}
                      size="small"
                    />
                  </Stack>

                  <Typography sx={{ mb: 2 }}>
                    {issue.description}
                  </Typography>

                  {issue.file && (
                    <Typography
                      variant="body2"
                      sx={{
                        fontFamily: "monospace",
                      }}
                    >
                      📄 {issue.file}
                    </Typography>
                  )}

                  {issue.line > 0 && (
                    <Chip
                      label={`Line ${issue.line}`}
                      size="small"
                      sx={{ mt: 1 }}
                    />
                  )}
                </Paper>
              ))}
            </Paper>

            {/* Recommendations */}
            <Paper
              variant="outlined"
              sx={{
                p: 3,
                borderRadius: 2,
              }}
            >
              <Typography variant="h6" gutterBottom>
                Recommendations
              </Typography>

              {reviewResult.recommendations.map(
                (item, index) => (
                  <Typography
                    key={index}
                    sx={{ mb: 1 }}
                  >
                    • {item}
                  </Typography>
                )
              )}
            </Paper>
          </>
        )}
      </Stack>
    </Paper>
  );
}

export default RepositoryForm;