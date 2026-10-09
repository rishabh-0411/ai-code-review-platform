import { Container, Typography } from "@mui/material";
import RepositoryForm from "../components/RepositoryForm";

function Home() {
  return (
    <Container maxWidth="md" sx={{ mt: 5 }}>
      <Typography
        variant="h3"
        gutterBottom
        align="center"
      >
        AI Code Review Platform
      </Typography>

      <RepositoryForm />
    </Container>
  );
}

export default Home;